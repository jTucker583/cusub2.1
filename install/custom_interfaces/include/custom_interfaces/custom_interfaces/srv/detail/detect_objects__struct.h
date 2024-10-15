// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:srv/DetectObjects.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__STRUCT_H_
#define CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/DetectObjects in the package custom_interfaces.
typedef struct custom_interfaces__srv__DetectObjects_Request
{
  uint8_t structure_needs_at_least_one_member;
} custom_interfaces__srv__DetectObjects_Request;

// Struct for a sequence of custom_interfaces__srv__DetectObjects_Request.
typedef struct custom_interfaces__srv__DetectObjects_Request__Sequence
{
  custom_interfaces__srv__DetectObjects_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__DetectObjects_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'object_names'
#include "rosidl_runtime_c/string.h"
// Member 'object_positions_x'
// Member 'object_positions_y'
// Member 'confidence'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/DetectObjects in the package custom_interfaces.
typedef struct custom_interfaces__srv__DetectObjects_Response
{
  /// Response: Detected object names, positions, and confidence scores
  rosidl_runtime_c__String__Sequence object_names;
  rosidl_runtime_c__float__Sequence object_positions_x;
  rosidl_runtime_c__float__Sequence object_positions_y;
  rosidl_runtime_c__float__Sequence confidence;
} custom_interfaces__srv__DetectObjects_Response;

// Struct for a sequence of custom_interfaces__srv__DetectObjects_Response.
typedef struct custom_interfaces__srv__DetectObjects_Response__Sequence
{
  custom_interfaces__srv__DetectObjects_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__DetectObjects_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__STRUCT_H_
