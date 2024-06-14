#!/usr/bin/python3

import argparse
import csv
import datetime
import json
import socket


class _CSVWriter:
    def __init__(self, csv_file, message_type):
        self.csv_file = csv_file
        self.csv_writer = self._csv_writer(csv_file, message_type)

    @classmethod
    def _csv_field_names(cls, message_type):
        if message_type == "velocity":
            return [
                "log_time",
                "time_of_validity",
                "time_of_transmission",
                "time",
                "vx",
                "vy",
                "vz",
                "fom",
                "altitude",
                "velocity_valid",
                "status" ]
        return [
            "log_time",
            "ts",
            "x",
            "y",
            "z",
            "std",
            "status" ]

    @classmethod
    def _csv_writer(cls, csv_file, message_type):
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames = cls._csv_field_names(message_type),
            extrasaction = "ignore",
            delimiter = ',')
        csv_writer.writeheader()
        return csv_writer

    def writerow(self, row):
        self.csv_writer.writerow(row)

    def flush(self):
        self.csv_file.flush()


class _DVLMessage:
    def __init__(self, ip="192.168.194.95"):
        self.message = None
        self.dvl = None
        self.ip = ip
        self.readingdata = False

    def __str__(self):
        return json.dumps(self.message)
    
    def _start_dvl_socket(self):
        try:
            dvl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            dvl_socket.connect((self.ip, 16171))
            return dvl_socket
        except ConnectionRefusedError:
            return ConnectionRefusedError

    def _type(self, message_type):
        if message_type == "velocity":
            return "velocity"
        return "position_local"

    def _format_timestamp(self, timestamp, time_format):
        return datetime.datetime.strftime(
            datetime.datetime.fromtimestamp(timestamp),
            time_format)

    def _format_timestamps(self, message_type, message, time_format):
        message["log_time"] = self._format_timestamp(
            message["log_time"] / 1e6,
            time_format)
        if message_type == "velocity":
            try:
                message["time_of_validity"] = self._format_timestamp(
                    message["time_of_validity"] / 1e6,
                    time_format)
                message["time_of_transmission"] = self._format_timestamp(
                    message["time_of_transmission"] / 1e6,
                    time_format)
            except KeyError:
                pass
        else:
            message["ts"] = self._format_timestamp(message["ts"], time_format)

    def _handle(self, message_type, message, time_format, csv_writer):
        """Handle a message from the DVL. Set self.message to the message."""
        if not message:
            return
        try:
            report = json.loads(message)
        except json.decoder.JSONDecodeError:
            print("Could not parse to JSON: " + message)
            return
        if report["type"] != message_type:
            return
        report["log_time"] = int(datetime.datetime.utcnow().timestamp() * 1e6)
        if time_format:
            self._format_timestamps(message_type, report, time_format)
        self.message = (json.dumps(report)) # the key function to return all data
        # if csv_writer is not None:
        #     csv_writer.writerow(report)
        #     csv_writer.flush()

    def _process_messages(self, dvl_socket, message_type, time_format, csv_writer = None):
        """Read messages from the DVL and process them."""
        buffer_size = 4096
        message = ""
        while self.readingdata:
            buffer = dvl_socket.recv(buffer_size).decode()
            if not buffer:
                continue
            message_parts = buffer.split("\r\n")
            if len(message_parts) == 1:
                message += message_parts[0]
                continue
            for message_part in message_parts[:-1]:
                message = message + message_part
                self._handle(message_type, message, time_format, csv_writer)
                message = ""
            if message_parts[-1]:
                message = message_parts[-1]

    def startReading(self, message_type, time_format="%Y-%m-%d %H:%M:%S"):
        self.readingdata = True
        self.dvl = self._start_dvl_socket()
        if self.dvl == ConnectionRefusedError:
            return ConnectionRefusedError
        self._process_messages(
            self.dvl,
            self._type(message_type),
            time_format)
        
    def stopReading(self):
        self.readingdata = False

    def readMessage(self):
        return self.message
