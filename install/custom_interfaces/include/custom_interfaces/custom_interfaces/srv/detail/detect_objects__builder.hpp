// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/DetectObjects.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/srv/detail/detect_objects__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::DetectObjects_Request>()
{
  return ::custom_interfaces::srv::DetectObjects_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_DetectObjects_Response_confidence
{
public:
  explicit Init_DetectObjects_Response_confidence(::custom_interfaces::srv::DetectObjects_Response & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::srv::DetectObjects_Response confidence(::custom_interfaces::srv::DetectObjects_Response::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::DetectObjects_Response msg_;
};

class Init_DetectObjects_Response_object_positions_y
{
public:
  explicit Init_DetectObjects_Response_object_positions_y(::custom_interfaces::srv::DetectObjects_Response & msg)
  : msg_(msg)
  {}
  Init_DetectObjects_Response_confidence object_positions_y(::custom_interfaces::srv::DetectObjects_Response::_object_positions_y_type arg)
  {
    msg_.object_positions_y = std::move(arg);
    return Init_DetectObjects_Response_confidence(msg_);
  }

private:
  ::custom_interfaces::srv::DetectObjects_Response msg_;
};

class Init_DetectObjects_Response_object_positions_x
{
public:
  explicit Init_DetectObjects_Response_object_positions_x(::custom_interfaces::srv::DetectObjects_Response & msg)
  : msg_(msg)
  {}
  Init_DetectObjects_Response_object_positions_y object_positions_x(::custom_interfaces::srv::DetectObjects_Response::_object_positions_x_type arg)
  {
    msg_.object_positions_x = std::move(arg);
    return Init_DetectObjects_Response_object_positions_y(msg_);
  }

private:
  ::custom_interfaces::srv::DetectObjects_Response msg_;
};

class Init_DetectObjects_Response_object_names
{
public:
  Init_DetectObjects_Response_object_names()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DetectObjects_Response_object_positions_x object_names(::custom_interfaces::srv::DetectObjects_Response::_object_names_type arg)
  {
    msg_.object_names = std::move(arg);
    return Init_DetectObjects_Response_object_positions_x(msg_);
  }

private:
  ::custom_interfaces::srv::DetectObjects_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::DetectObjects_Response>()
{
  return custom_interfaces::srv::builder::Init_DetectObjects_Response_object_names();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__BUILDER_HPP_
