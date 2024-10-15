// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_interfaces:srv/DetectObjects.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__TRAITS_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "custom_interfaces/srv/detail/detect_objects__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace custom_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const DetectObjects_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DetectObjects_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DetectObjects_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace custom_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use custom_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const custom_interfaces::srv::DetectObjects_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const custom_interfaces::srv::DetectObjects_Request & msg)
{
  return custom_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<custom_interfaces::srv::DetectObjects_Request>()
{
  return "custom_interfaces::srv::DetectObjects_Request";
}

template<>
inline const char * name<custom_interfaces::srv::DetectObjects_Request>()
{
  return "custom_interfaces/srv/DetectObjects_Request";
}

template<>
struct has_fixed_size<custom_interfaces::srv::DetectObjects_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<custom_interfaces::srv::DetectObjects_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<custom_interfaces::srv::DetectObjects_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace custom_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const DetectObjects_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: object_names
  {
    if (msg.object_names.size() == 0) {
      out << "object_names: []";
    } else {
      out << "object_names: [";
      size_t pending_items = msg.object_names.size();
      for (auto item : msg.object_names) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: object_positions_x
  {
    if (msg.object_positions_x.size() == 0) {
      out << "object_positions_x: []";
    } else {
      out << "object_positions_x: [";
      size_t pending_items = msg.object_positions_x.size();
      for (auto item : msg.object_positions_x) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: object_positions_y
  {
    if (msg.object_positions_y.size() == 0) {
      out << "object_positions_y: []";
    } else {
      out << "object_positions_y: [";
      size_t pending_items = msg.object_positions_y.size();
      for (auto item : msg.object_positions_y) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: confidence
  {
    if (msg.confidence.size() == 0) {
      out << "confidence: []";
    } else {
      out << "confidence: [";
      size_t pending_items = msg.confidence.size();
      for (auto item : msg.confidence) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DetectObjects_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: object_names
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.object_names.size() == 0) {
      out << "object_names: []\n";
    } else {
      out << "object_names:\n";
      for (auto item : msg.object_names) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: object_positions_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.object_positions_x.size() == 0) {
      out << "object_positions_x: []\n";
    } else {
      out << "object_positions_x:\n";
      for (auto item : msg.object_positions_x) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: object_positions_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.object_positions_y.size() == 0) {
      out << "object_positions_y: []\n";
    } else {
      out << "object_positions_y:\n";
      for (auto item : msg.object_positions_y) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.confidence.size() == 0) {
      out << "confidence: []\n";
    } else {
      out << "confidence:\n";
      for (auto item : msg.confidence) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DetectObjects_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace custom_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use custom_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const custom_interfaces::srv::DetectObjects_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const custom_interfaces::srv::DetectObjects_Response & msg)
{
  return custom_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<custom_interfaces::srv::DetectObjects_Response>()
{
  return "custom_interfaces::srv::DetectObjects_Response";
}

template<>
inline const char * name<custom_interfaces::srv::DetectObjects_Response>()
{
  return "custom_interfaces/srv/DetectObjects_Response";
}

template<>
struct has_fixed_size<custom_interfaces::srv::DetectObjects_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<custom_interfaces::srv::DetectObjects_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<custom_interfaces::srv::DetectObjects_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_interfaces::srv::DetectObjects>()
{
  return "custom_interfaces::srv::DetectObjects";
}

template<>
inline const char * name<custom_interfaces::srv::DetectObjects>()
{
  return "custom_interfaces/srv/DetectObjects";
}

template<>
struct has_fixed_size<custom_interfaces::srv::DetectObjects>
  : std::integral_constant<
    bool,
    has_fixed_size<custom_interfaces::srv::DetectObjects_Request>::value &&
    has_fixed_size<custom_interfaces::srv::DetectObjects_Response>::value
  >
{
};

template<>
struct has_bounded_size<custom_interfaces::srv::DetectObjects>
  : std::integral_constant<
    bool,
    has_bounded_size<custom_interfaces::srv::DetectObjects_Request>::value &&
    has_bounded_size<custom_interfaces::srv::DetectObjects_Response>::value
  >
{
};

template<>
struct is_service<custom_interfaces::srv::DetectObjects>
  : std::true_type
{
};

template<>
struct is_service_request<custom_interfaces::srv::DetectObjects_Request>
  : std::true_type
{
};

template<>
struct is_service_response<custom_interfaces::srv::DetectObjects_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__DETECT_OBJECTS__TRAITS_HPP_
