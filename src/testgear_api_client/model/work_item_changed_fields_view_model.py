"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from testgear_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from testgear_api_client.exceptions import ApiAttributeError


def lazy_import():
    from testgear_api_client.model.attachment_change_view_model_array_work_item_changed_field_view_model import AttachmentChangeViewModelArrayWorkItemChangedFieldViewModel
    from testgear_api_client.model.auto_test_change_view_model_array_work_item_changed_field_view_model import AutoTestChangeViewModelArrayWorkItemChangedFieldViewModel
    from testgear_api_client.model.boolean_work_item_changed_field_view_model import BooleanWorkItemChangedFieldViewModel
    from testgear_api_client.model.guid_work_item_changed_field_view_model import GuidWorkItemChangedFieldViewModel
    from testgear_api_client.model.int32_work_item_changed_field_view_model import Int32WorkItemChangedFieldViewModel
    from testgear_api_client.model.int64_work_item_changed_field_view_model import Int64WorkItemChangedFieldViewModel
    from testgear_api_client.model.string_array_work_item_changed_field_view_model import StringArrayWorkItemChangedFieldViewModel
    from testgear_api_client.model.string_work_item_changed_field_view_model import StringWorkItemChangedFieldViewModel
    from testgear_api_client.model.work_item_changed_attribute_view_model import WorkItemChangedAttributeViewModel
    from testgear_api_client.model.work_item_link_change_view_model_array_work_item_changed_field_view_model import WorkItemLinkChangeViewModelArrayWorkItemChangedFieldViewModel
    from testgear_api_client.model.work_item_step_change_view_model_array_work_item_changed_field_view_model import WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel
    globals()['AttachmentChangeViewModelArrayWorkItemChangedFieldViewModel'] = AttachmentChangeViewModelArrayWorkItemChangedFieldViewModel
    globals()['AutoTestChangeViewModelArrayWorkItemChangedFieldViewModel'] = AutoTestChangeViewModelArrayWorkItemChangedFieldViewModel
    globals()['BooleanWorkItemChangedFieldViewModel'] = BooleanWorkItemChangedFieldViewModel
    globals()['GuidWorkItemChangedFieldViewModel'] = GuidWorkItemChangedFieldViewModel
    globals()['Int32WorkItemChangedFieldViewModel'] = Int32WorkItemChangedFieldViewModel
    globals()['Int64WorkItemChangedFieldViewModel'] = Int64WorkItemChangedFieldViewModel
    globals()['StringArrayWorkItemChangedFieldViewModel'] = StringArrayWorkItemChangedFieldViewModel
    globals()['StringWorkItemChangedFieldViewModel'] = StringWorkItemChangedFieldViewModel
    globals()['WorkItemChangedAttributeViewModel'] = WorkItemChangedAttributeViewModel
    globals()['WorkItemLinkChangeViewModelArrayWorkItemChangedFieldViewModel'] = WorkItemLinkChangeViewModelArrayWorkItemChangedFieldViewModel
    globals()['WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel'] = WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel


class WorkItemChangedFieldsViewModel(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'name': (StringWorkItemChangedFieldViewModel,),  # noqa: E501
            'is_deleted': (BooleanWorkItemChangedFieldViewModel,),  # noqa: E501
            'project_id': (GuidWorkItemChangedFieldViewModel,),  # noqa: E501
            'is_automated': (BooleanWorkItemChangedFieldViewModel,),  # noqa: E501
            'section_id': (GuidWorkItemChangedFieldViewModel,),  # noqa: E501
            'description': (StringWorkItemChangedFieldViewModel,),  # noqa: E501
            'state': (StringWorkItemChangedFieldViewModel,),  # noqa: E501
            'priority': (StringWorkItemChangedFieldViewModel,),  # noqa: E501
            'duration': (Int32WorkItemChangedFieldViewModel,),  # noqa: E501
            'attributes': ({str: (WorkItemChangedAttributeViewModel,)}, none_type,),  # noqa: E501
            'steps': (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel,),  # noqa: E501
            'precondition_steps': (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel,),  # noqa: E501
            'postcondition_steps': (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel,),  # noqa: E501
            'auto_tests': (AutoTestChangeViewModelArrayWorkItemChangedFieldViewModel,),  # noqa: E501
            'attachments': (AttachmentChangeViewModelArrayWorkItemChangedFieldViewModel,),  # noqa: E501
            'tags': (StringArrayWorkItemChangedFieldViewModel,),  # noqa: E501
            'links': (WorkItemLinkChangeViewModelArrayWorkItemChangedFieldViewModel,),  # noqa: E501
            'global_id': (Int64WorkItemChangedFieldViewModel,),  # noqa: E501
            'version_number': (Int32WorkItemChangedFieldViewModel,),  # noqa: E501
            'entity_type_name': (StringWorkItemChangedFieldViewModel,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'is_deleted': 'isDeleted',  # noqa: E501
        'project_id': 'projectId',  # noqa: E501
        'is_automated': 'isAutomated',  # noqa: E501
        'section_id': 'sectionId',  # noqa: E501
        'description': 'description',  # noqa: E501
        'state': 'state',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'duration': 'duration',  # noqa: E501
        'attributes': 'attributes',  # noqa: E501
        'steps': 'steps',  # noqa: E501
        'precondition_steps': 'preconditionSteps',  # noqa: E501
        'postcondition_steps': 'postconditionSteps',  # noqa: E501
        'auto_tests': 'autoTests',  # noqa: E501
        'attachments': 'attachments',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'links': 'links',  # noqa: E501
        'global_id': 'globalId',  # noqa: E501
        'version_number': 'versionNumber',  # noqa: E501
        'entity_type_name': 'entityTypeName',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """WorkItemChangedFieldsViewModel - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            is_deleted (BooleanWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            project_id (GuidWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            is_automated (BooleanWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            section_id (GuidWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            description (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            state (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            priority (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            duration (Int32WorkItemChangedFieldViewModel): [optional]  # noqa: E501
            attributes ({str: (WorkItemChangedAttributeViewModel,)}, none_type): [optional]  # noqa: E501
            steps (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            precondition_steps (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            postcondition_steps (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            auto_tests (AutoTestChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            attachments (AttachmentChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            tags (StringArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            links (WorkItemLinkChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            global_id (Int64WorkItemChangedFieldViewModel): [optional]  # noqa: E501
            version_number (Int32WorkItemChangedFieldViewModel): [optional]  # noqa: E501
            entity_type_name (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """WorkItemChangedFieldsViewModel - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            is_deleted (BooleanWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            project_id (GuidWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            is_automated (BooleanWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            section_id (GuidWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            description (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            state (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            priority (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            duration (Int32WorkItemChangedFieldViewModel): [optional]  # noqa: E501
            attributes ({str: (WorkItemChangedAttributeViewModel,)}, none_type): [optional]  # noqa: E501
            steps (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            precondition_steps (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            postcondition_steps (WorkItemStepChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            auto_tests (AutoTestChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            attachments (AttachmentChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            tags (StringArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            links (WorkItemLinkChangeViewModelArrayWorkItemChangedFieldViewModel): [optional]  # noqa: E501
            global_id (Int64WorkItemChangedFieldViewModel): [optional]  # noqa: E501
            version_number (Int32WorkItemChangedFieldViewModel): [optional]  # noqa: E501
            entity_type_name (StringWorkItemChangedFieldViewModel): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
