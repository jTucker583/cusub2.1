// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from custom_interfaces:srv/DetectObjects.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "custom_interfaces/srv/detail/detect_objects__rosidl_typesupport_introspection_c.h"
#include "custom_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "custom_interfaces/srv/detail/detect_objects__functions.h"
#include "custom_interfaces/srv/detail/detect_objects__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  custom_interfaces__srv__DetectObjects_Request__init(message_memory);
}

void custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_fini_function(void * message_memory)
{
  custom_interfaces__srv__DetectObjects_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_interfaces__srv__DetectObjects_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_message_members = {
  "custom_interfaces__srv",  // message namespace
  "DetectObjects_Request",  // message name
  1,  // number of fields
  sizeof(custom_interfaces__srv__DetectObjects_Request),
  custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_message_member_array,  // message members
  custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_message_type_support_handle = {
  0,
  &custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_custom_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_interfaces, srv, DetectObjects_Request)() {
  if (!custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_message_type_support_handle.typesupport_identifier) {
    custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &custom_interfaces__srv__DetectObjects_Request__rosidl_typesupport_introspection_c__DetectObjects_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "custom_interfaces/srv/detail/detect_objects__rosidl_typesupport_introspection_c.h"
// already included above
// #include "custom_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "custom_interfaces/srv/detail/detect_objects__functions.h"
// already included above
// #include "custom_interfaces/srv/detail/detect_objects__struct.h"


// Include directives for member types
// Member `object_names`
#include "rosidl_runtime_c/string_functions.h"
// Member `object_positions_x`
// Member `object_positions_y`
// Member `confidence`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  custom_interfaces__srv__DetectObjects_Response__init(message_memory);
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_fini_function(void * message_memory)
{
  custom_interfaces__srv__DetectObjects_Response__fini(message_memory);
}

size_t custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__size_function__DetectObjects_Response__object_names(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_names(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_names(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__fetch_function__DetectObjects_Response__object_names(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_names(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__assign_function__DetectObjects_Response__object_names(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_names(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__resize_function__DetectObjects_Response__object_names(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__size_function__DetectObjects_Response__object_positions_x(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_positions_x(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_positions_x(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__fetch_function__DetectObjects_Response__object_positions_x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_positions_x(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__assign_function__DetectObjects_Response__object_positions_x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_positions_x(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__resize_function__DetectObjects_Response__object_positions_x(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__size_function__DetectObjects_Response__object_positions_y(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_positions_y(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_positions_y(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__fetch_function__DetectObjects_Response__object_positions_y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_positions_y(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__assign_function__DetectObjects_Response__object_positions_y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_positions_y(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__resize_function__DetectObjects_Response__object_positions_y(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__size_function__DetectObjects_Response__confidence(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__confidence(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__confidence(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__fetch_function__DetectObjects_Response__confidence(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__confidence(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__assign_function__DetectObjects_Response__confidence(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__confidence(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__resize_function__DetectObjects_Response__confidence(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_message_member_array[4] = {
  {
    "object_names",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_interfaces__srv__DetectObjects_Response, object_names),  // bytes offset in struct
    NULL,  // default value
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__size_function__DetectObjects_Response__object_names,  // size() function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_names,  // get_const(index) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_names,  // get(index) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__fetch_function__DetectObjects_Response__object_names,  // fetch(index, &value) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__assign_function__DetectObjects_Response__object_names,  // assign(index, value) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__resize_function__DetectObjects_Response__object_names  // resize(index) function pointer
  },
  {
    "object_positions_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_interfaces__srv__DetectObjects_Response, object_positions_x),  // bytes offset in struct
    NULL,  // default value
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__size_function__DetectObjects_Response__object_positions_x,  // size() function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_positions_x,  // get_const(index) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_positions_x,  // get(index) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__fetch_function__DetectObjects_Response__object_positions_x,  // fetch(index, &value) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__assign_function__DetectObjects_Response__object_positions_x,  // assign(index, value) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__resize_function__DetectObjects_Response__object_positions_x  // resize(index) function pointer
  },
  {
    "object_positions_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_interfaces__srv__DetectObjects_Response, object_positions_y),  // bytes offset in struct
    NULL,  // default value
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__size_function__DetectObjects_Response__object_positions_y,  // size() function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__object_positions_y,  // get_const(index) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__object_positions_y,  // get(index) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__fetch_function__DetectObjects_Response__object_positions_y,  // fetch(index, &value) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__assign_function__DetectObjects_Response__object_positions_y,  // assign(index, value) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__resize_function__DetectObjects_Response__object_positions_y  // resize(index) function pointer
  },
  {
    "confidence",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_interfaces__srv__DetectObjects_Response, confidence),  // bytes offset in struct
    NULL,  // default value
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__size_function__DetectObjects_Response__confidence,  // size() function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_const_function__DetectObjects_Response__confidence,  // get_const(index) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__get_function__DetectObjects_Response__confidence,  // get(index) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__fetch_function__DetectObjects_Response__confidence,  // fetch(index, &value) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__assign_function__DetectObjects_Response__confidence,  // assign(index, value) function pointer
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__resize_function__DetectObjects_Response__confidence  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_message_members = {
  "custom_interfaces__srv",  // message namespace
  "DetectObjects_Response",  // message name
  4,  // number of fields
  sizeof(custom_interfaces__srv__DetectObjects_Response),
  custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_message_member_array,  // message members
  custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_message_type_support_handle = {
  0,
  &custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_custom_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_interfaces, srv, DetectObjects_Response)() {
  if (!custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_message_type_support_handle.typesupport_identifier) {
    custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &custom_interfaces__srv__DetectObjects_Response__rosidl_typesupport_introspection_c__DetectObjects_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "custom_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "custom_interfaces/srv/detail/detect_objects__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_service_members = {
  "custom_interfaces__srv",  // service namespace
  "DetectObjects",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_Request_message_type_support_handle,
  NULL  // response message
  // custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_Response_message_type_support_handle
};

static rosidl_service_type_support_t custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_service_type_support_handle = {
  0,
  &custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_interfaces, srv, DetectObjects_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_interfaces, srv, DetectObjects_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_custom_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_interfaces, srv, DetectObjects)() {
  if (!custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_service_type_support_handle.typesupport_identifier) {
    custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_interfaces, srv, DetectObjects_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_interfaces, srv, DetectObjects_Response)()->data;
  }

  return &custom_interfaces__srv__detail__detect_objects__rosidl_typesupport_introspection_c__DetectObjects_service_type_support_handle;
}
