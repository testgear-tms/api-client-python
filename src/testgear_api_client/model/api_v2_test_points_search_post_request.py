"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from testit_api_client.model_utils import (  # noqa: F401
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
from testit_api_client.exceptions import ApiAttributeError


def lazy_import():
    from testit_api_client.model.test_point_filter_model import TestPointFilterModel
    from testit_api_client.model.test_point_filter_model_created_date import TestPointFilterModelCreatedDate
    from testit_api_client.model.test_point_filter_model_duration import TestPointFilterModelDuration
    from testit_api_client.model.test_point_filter_model_modified_date import TestPointFilterModelModifiedDate
    from testit_api_client.model.test_point_filter_model_work_item_created_date import TestPointFilterModelWorkItemCreatedDate
    from testit_api_client.model.test_point_filter_model_work_item_median_duration import TestPointFilterModelWorkItemMedianDuration
    from testit_api_client.model.test_point_filter_model_work_item_modified_date import TestPointFilterModelWorkItemModifiedDate
    from testit_api_client.model.test_point_status import TestPointStatus
    from testit_api_client.model.work_item_priority_model import WorkItemPriorityModel
    globals()['TestPointFilterModel'] = TestPointFilterModel
    globals()['TestPointFilterModelCreatedDate'] = TestPointFilterModelCreatedDate
    globals()['TestPointFilterModelDuration'] = TestPointFilterModelDuration
    globals()['TestPointFilterModelModifiedDate'] = TestPointFilterModelModifiedDate
    globals()['TestPointFilterModelWorkItemCreatedDate'] = TestPointFilterModelWorkItemCreatedDate
    globals()['TestPointFilterModelWorkItemMedianDuration'] = TestPointFilterModelWorkItemMedianDuration
    globals()['TestPointFilterModelWorkItemModifiedDate'] = TestPointFilterModelWorkItemModifiedDate
    globals()['TestPointStatus'] = TestPointStatus
    globals()['WorkItemPriorityModel'] = WorkItemPriorityModel


class ApiV2TestPointsSearchPostRequest(ModelComposed):
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
        ('name',): {
            'max_length': 255,
            'min_length': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

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
            'test_plan_ids': ([str], none_type,),  # noqa: E501
            'test_suite_ids': ([str], none_type,),  # noqa: E501
            'work_item_global_ids': ([int], none_type,),  # noqa: E501
            'work_item_median_duration': (TestPointFilterModelWorkItemMedianDuration,),  # noqa: E501
            'statuses': ([TestPointStatus], none_type,),  # noqa: E501
            'priorities': ([WorkItemPriorityModel], none_type,),  # noqa: E501
            'is_automated': (bool, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'configuration_ids': ([str], none_type,),  # noqa: E501
            'tester_ids': ([str], none_type,),  # noqa: E501
            'duration': (TestPointFilterModelDuration,),  # noqa: E501
            'section_ids': ([str], none_type,),  # noqa: E501
            'created_date': (TestPointFilterModelCreatedDate,),  # noqa: E501
            'created_by_ids': ([str], none_type,),  # noqa: E501
            'modified_date': (TestPointFilterModelModifiedDate,),  # noqa: E501
            'modified_by_ids': ([str], none_type,),  # noqa: E501
            'tags': ([str], none_type,),  # noqa: E501
            'attributes': ({str: ([str],)}, none_type,),  # noqa: E501
            'work_item_created_date': (TestPointFilterModelWorkItemCreatedDate,),  # noqa: E501
            'work_item_created_by_ids': ([str], none_type,),  # noqa: E501
            'work_item_modified_date': (TestPointFilterModelWorkItemModifiedDate,),  # noqa: E501
            'work_item_modified_by_ids': ([str], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'test_plan_ids': 'testPlanIds',  # noqa: E501
        'test_suite_ids': 'testSuiteIds',  # noqa: E501
        'work_item_global_ids': 'workItemGlobalIds',  # noqa: E501
        'work_item_median_duration': 'workItemMedianDuration',  # noqa: E501
        'statuses': 'statuses',  # noqa: E501
        'priorities': 'priorities',  # noqa: E501
        'is_automated': 'isAutomated',  # noqa: E501
        'name': 'name',  # noqa: E501
        'configuration_ids': 'configurationIds',  # noqa: E501
        'tester_ids': 'testerIds',  # noqa: E501
        'duration': 'duration',  # noqa: E501
        'section_ids': 'sectionIds',  # noqa: E501
        'created_date': 'createdDate',  # noqa: E501
        'created_by_ids': 'createdByIds',  # noqa: E501
        'modified_date': 'modifiedDate',  # noqa: E501
        'modified_by_ids': 'modifiedByIds',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'attributes': 'attributes',  # noqa: E501
        'work_item_created_date': 'workItemCreatedDate',  # noqa: E501
        'work_item_created_by_ids': 'workItemCreatedByIds',  # noqa: E501
        'work_item_modified_date': 'workItemModifiedDate',  # noqa: E501
        'work_item_modified_by_ids': 'workItemModifiedByIds',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ApiV2TestPointsSearchPostRequest - a model defined in OpenAPI

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
            test_plan_ids ([str], none_type): Specifies a test point test plan IDS to search for. [optional]  # noqa: E501
            test_suite_ids ([str], none_type): Specifies a test point test suite IDs to search for. [optional]  # noqa: E501
            work_item_global_ids ([int], none_type): Specifies a test point work item global IDs to search for. [optional]  # noqa: E501
            work_item_median_duration (TestPointFilterModelWorkItemMedianDuration): [optional]  # noqa: E501
            statuses ([TestPointStatus], none_type): Specifies a test point statuses to search for. [optional]  # noqa: E501
            priorities ([WorkItemPriorityModel], none_type): Specifies a test point priorities to search for. [optional]  # noqa: E501
            is_automated (bool, none_type): Specifies a test point automation status to search for. [optional]  # noqa: E501
            name (str, none_type): Specifies a test point name to search for. [optional]  # noqa: E501
            configuration_ids ([str], none_type): Specifies a test point configuration IDs to search for. [optional]  # noqa: E501
            tester_ids ([str], none_type): Specifies a test point assigned user IDs to search for. [optional]  # noqa: E501
            duration (TestPointFilterModelDuration): [optional]  # noqa: E501
            section_ids ([str], none_type): Specifies a test point work item section IDs to search for. [optional]  # noqa: E501
            created_date (TestPointFilterModelCreatedDate): [optional]  # noqa: E501
            created_by_ids ([str], none_type): Specifies a test point creator IDs to search for. [optional]  # noqa: E501
            modified_date (TestPointFilterModelModifiedDate): [optional]  # noqa: E501
            modified_by_ids ([str], none_type): Specifies a test point last editor IDs to search for. [optional]  # noqa: E501
            tags ([str], none_type): Specifies a test point tags to search for. [optional]  # noqa: E501
            attributes ({str: ([str],)}, none_type): Specifies a test point attributes to search for. [optional]  # noqa: E501
            work_item_created_date (TestPointFilterModelWorkItemCreatedDate): [optional]  # noqa: E501
            work_item_created_by_ids ([str], none_type): Specifies a work item creator IDs to search for. [optional]  # noqa: E501
            work_item_modified_date (TestPointFilterModelWorkItemModifiedDate): [optional]  # noqa: E501
            work_item_modified_by_ids ([str], none_type): Specifies a work item last editor IDs to search for. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ApiV2TestPointsSearchPostRequest - a model defined in OpenAPI

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
            test_plan_ids ([str], none_type): Specifies a test point test plan IDS to search for. [optional]  # noqa: E501
            test_suite_ids ([str], none_type): Specifies a test point test suite IDs to search for. [optional]  # noqa: E501
            work_item_global_ids ([int], none_type): Specifies a test point work item global IDs to search for. [optional]  # noqa: E501
            work_item_median_duration (TestPointFilterModelWorkItemMedianDuration): [optional]  # noqa: E501
            statuses ([TestPointStatus], none_type): Specifies a test point statuses to search for. [optional]  # noqa: E501
            priorities ([WorkItemPriorityModel], none_type): Specifies a test point priorities to search for. [optional]  # noqa: E501
            is_automated (bool, none_type): Specifies a test point automation status to search for. [optional]  # noqa: E501
            name (str, none_type): Specifies a test point name to search for. [optional]  # noqa: E501
            configuration_ids ([str], none_type): Specifies a test point configuration IDs to search for. [optional]  # noqa: E501
            tester_ids ([str], none_type): Specifies a test point assigned user IDs to search for. [optional]  # noqa: E501
            duration (TestPointFilterModelDuration): [optional]  # noqa: E501
            section_ids ([str], none_type): Specifies a test point work item section IDs to search for. [optional]  # noqa: E501
            created_date (TestPointFilterModelCreatedDate): [optional]  # noqa: E501
            created_by_ids ([str], none_type): Specifies a test point creator IDs to search for. [optional]  # noqa: E501
            modified_date (TestPointFilterModelModifiedDate): [optional]  # noqa: E501
            modified_by_ids ([str], none_type): Specifies a test point last editor IDs to search for. [optional]  # noqa: E501
            tags ([str], none_type): Specifies a test point tags to search for. [optional]  # noqa: E501
            attributes ({str: ([str],)}, none_type): Specifies a test point attributes to search for. [optional]  # noqa: E501
            work_item_created_date (TestPointFilterModelWorkItemCreatedDate): [optional]  # noqa: E501
            work_item_created_by_ids ([str], none_type): Specifies a work item creator IDs to search for. [optional]  # noqa: E501
            work_item_modified_date (TestPointFilterModelWorkItemModifiedDate): [optional]  # noqa: E501
            work_item_modified_by_ids ([str], none_type): Specifies a work item last editor IDs to search for. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              TestPointFilterModel,
          ],
          'oneOf': [
          ],
        }
