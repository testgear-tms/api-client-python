
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from testgear_api_client.api.attachments_api import AttachmentsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from testgear_api_client.api.attachments_api import AttachmentsApi
from testgear_api_client.api.auto_tests_api import AutoTestsApi
from testgear_api_client.api.background_jobs_api import BackgroundJobsApi
from testgear_api_client.api.configurations_api import ConfigurationsApi
from testgear_api_client.api.custom_attribute_templates_api import CustomAttributeTemplatesApi
from testgear_api_client.api.custom_attributes_api import CustomAttributesApi
from testgear_api_client.api.notifications_api import NotificationsApi
from testgear_api_client.api.parameters_api import ParametersApi
from testgear_api_client.api.project_attribute_templates_api import ProjectAttributeTemplatesApi
from testgear_api_client.api.project_attributes_api import ProjectAttributesApi
from testgear_api_client.api.project_configurations_api import ProjectConfigurationsApi
from testgear_api_client.api.project_export_api import ProjectExportApi
from testgear_api_client.api.project_import_api import ProjectImportApi
from testgear_api_client.api.project_sections_api import ProjectSectionsApi
from testgear_api_client.api.project_test_plan_attributes_api import ProjectTestPlanAttributesApi
from testgear_api_client.api.project_test_plans_api import ProjectTestPlansApi
from testgear_api_client.api.project_work_items_api import ProjectWorkItemsApi
from testgear_api_client.api.projects_api import ProjectsApi
from testgear_api_client.api.search_api import SearchApi
from testgear_api_client.api.sections_api import SectionsApi
from testgear_api_client.api.tags_api import TagsApi
from testgear_api_client.api.test_plans_api import TestPlansApi
from testgear_api_client.api.test_points_api import TestPointsApi
from testgear_api_client.api.test_results_api import TestResultsApi
from testgear_api_client.api.test_runs_api import TestRunsApi
from testgear_api_client.api.test_suites_api import TestSuitesApi
from testgear_api_client.api.webhooks_api import WebhooksApi
from testgear_api_client.api.webhooks_logs_api import WebhooksLogsApi
from testgear_api_client.api.work_items_api import WorkItemsApi
from testgear_api_client.api.work_items_comments_api import WorkItemsCommentsApi
