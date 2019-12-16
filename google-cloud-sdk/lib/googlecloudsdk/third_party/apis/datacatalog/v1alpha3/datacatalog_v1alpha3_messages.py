"""Generated message classes for datacatalog version v1alpha3.

A fully managed and highly scalable data discovery and metadata management
service.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'datacatalog'


class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    condition: The condition that is associated with this binding. NOTE: An
      unsatisfied condition will not allow user access via current binding.
      Different bindings, including their conditions, are examined
      independently.
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example,
      `alice@example.com` .   * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.
      * `domain:{domain}`: The G Suite domain (primary) that represents all
      the    users of that domain. For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('Expr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class DatacatalogProjectsCrawlersCrawlerRunsGetRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersCrawlerRunsGetRequest object.

  Fields:
    name: Required. Resource name of the crawler run to retrieve. For example,
      "projects/project1/crawlers/crawler1/crawlerRuns/run1".
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsCrawlersCrawlerRunsListRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersCrawlerRunsListRequest object.

  Fields:
    pageSize: The maximum number of items to return. The default value for
      this field is 10. The maximum value for this field is 1000.
    pageToken: The next_page_token value returned from a previous list
      request, if any.
    parent: Required. Resource name of the parent crawler resource. For
      example, "projects/project1/crawlers/crawler1".
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class DatacatalogProjectsCrawlersCreateRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersCreateRequest object.

  Fields:
    crawlerId: Required. The id of the crawler to create.
    googleCloudDatacatalogV1alpha3Crawler: A
      GoogleCloudDatacatalogV1alpha3Crawler resource to be passed as the
      request body.
    parent: Required. The name of the project this crawler is in. Example:
      "projects/foo".
  """

  crawlerId = _messages.StringField(1)
  googleCloudDatacatalogV1alpha3Crawler = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Crawler', 2)
  parent = _messages.StringField(3, required=True)


class DatacatalogProjectsCrawlersDeleteRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersDeleteRequest object.

  Fields:
    name: Required. The resource name of the crawler. For example,
      "projects/bar/crawlers/foo".
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsCrawlersGetRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersGetRequest object.

  Fields:
    name: Required. The resource name of the crawler. For example,
      "projects/foo/crawlers/bar".
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsCrawlersListRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersListRequest object.

  Fields:
    pageSize: The maximum number of items to return. The default value for
      this field is 10. The maximum value for this field is 1000.
    pageToken: The next_page_token value returned from a previous list
      request, if any.
    parent: Required. The parent resource name. Example: "projects/foo".
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class DatacatalogProjectsCrawlersPatchRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersPatchRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3Crawler: A
      GoogleCloudDatacatalogV1alpha3Crawler resource to be passed as the
      request body.
    name: Output only. The resource name of the crawler. Must be empty when
      creating a crawler. For example, "projects/a/crawlers/b".
    updateMask: The update mask applies to the resource.
  """

  googleCloudDatacatalogV1alpha3Crawler = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Crawler', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class DatacatalogProjectsCrawlersRunRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersRunRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3RunCrawlerRequest: A
      GoogleCloudDatacatalogV1alpha3RunCrawlerRequest resource to be passed as
      the request body.
    name: Required. Resource name of the crawler resource. For example,
      "projects/project1/crawlers/crawler1".
  """

  googleCloudDatacatalogV1alpha3RunCrawlerRequest = _messages.MessageField('GoogleCloudDatacatalogV1alpha3RunCrawlerRequest', 1)
  name = _messages.StringField(2, required=True)


class DatacatalogProjectsTaxonomiesCategoriesCreateRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCategoriesCreateRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3Category: A
      GoogleCloudDatacatalogV1alpha3Category resource to be passed as the
      request body.
    parent: Required. Resource name of the taxonomy that the newly created
      category belongs to.
  """

  googleCloudDatacatalogV1alpha3Category = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Category', 1)
  parent = _messages.StringField(2, required=True)


class DatacatalogProjectsTaxonomiesCategoriesDeleteRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCategoriesDeleteRequest object.

  Fields:
    name: Required. Resource name of the category to be deleted. All its
      descendant categories will also be deleted.
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsTaxonomiesCategoriesGetIamPolicyRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCategoriesGetIamPolicyRequest object.

  Fields:
    getIamPolicyRequest: A GetIamPolicyRequest resource to be passed as the
      request body.
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  getIamPolicyRequest = _messages.MessageField('GetIamPolicyRequest', 1)
  resource = _messages.StringField(2, required=True)


class DatacatalogProjectsTaxonomiesCategoriesGetRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCategoriesGetRequest object.

  Fields:
    name: Required. Resource name of the category to be returned.
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsTaxonomiesCategoriesListRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCategoriesListRequest object.

  Fields:
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value returned from a previous List
      request, if any.
    parent: Required. Resource name of a taxonomy to list the categories of.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class DatacatalogProjectsTaxonomiesCategoriesPatchRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCategoriesPatchRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3Category: A
      GoogleCloudDatacatalogV1alpha3Category resource to be passed as the
      request body.
    name: Required. Resource name of the category to be updated.
    updateMask: The update mask applies to the resource. Only display_name,
      description and parent_category_id can be updated and thus can be listed
      in the mask. If update_mask is not provided, all allowed fields (i.e.
      display_name, description and parent_id) will be updated. For more
      information including the `FieldMask` definition, see
      https://developers.google.com/protocol-
      buffers/docs/reference/google.protobuf#fieldmask
  """

  googleCloudDatacatalogV1alpha3Category = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Category', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class DatacatalogProjectsTaxonomiesCategoriesSetIamPolicyRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCategoriesSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class DatacatalogProjectsTaxonomiesCategoriesTestIamPermissionsRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCategoriesTestIamPermissionsRequest
  object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class DatacatalogProjectsTaxonomiesCreateRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesCreateRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3Taxonomy: A
      GoogleCloudDatacatalogV1alpha3Taxonomy resource to be passed as the
      request body.
    parent: Required. Resource name of the project that the newly created
      taxonomy belongs to.
  """

  googleCloudDatacatalogV1alpha3Taxonomy = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Taxonomy', 1)
  parent = _messages.StringField(2, required=True)


class DatacatalogProjectsTaxonomiesDeleteRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesDeleteRequest object.

  Fields:
    name: Required. Resource name of the taxonomy to be deleted. All
      categories in this taxonomy will also be deleted.
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsTaxonomiesExportRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesExportRequest object.

  Fields:
    parent: Required. Resource name of the  project that taxonomies to be
      exported will share.
    taxonomyNames: Required. Resource names of the taxonomies to be exported.
  """

  parent = _messages.StringField(1, required=True)
  taxonomyNames = _messages.StringField(2, repeated=True)


class DatacatalogProjectsTaxonomiesGetIamPolicyRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesGetIamPolicyRequest object.

  Fields:
    getIamPolicyRequest: A GetIamPolicyRequest resource to be passed as the
      request body.
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  getIamPolicyRequest = _messages.MessageField('GetIamPolicyRequest', 1)
  resource = _messages.StringField(2, required=True)


class DatacatalogProjectsTaxonomiesGetRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesGetRequest object.

  Fields:
    name: Required. Resource name of the taxonomy to be returned.
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsTaxonomiesImportRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesImportRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3ImportTaxonomiesRequest: A
      GoogleCloudDatacatalogV1alpha3ImportTaxonomiesRequest resource to be
      passed as the request body.
    parent: Required. Resource name of project that the newly created
      taxonomies will belong to.
  """

  googleCloudDatacatalogV1alpha3ImportTaxonomiesRequest = _messages.MessageField('GoogleCloudDatacatalogV1alpha3ImportTaxonomiesRequest', 1)
  parent = _messages.StringField(2, required=True)


class DatacatalogProjectsTaxonomiesListRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesListRequest object.

  Fields:
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value returned from a previous list
      request, if any.
    parent: Required. Resource name of a project to list the taxonomies of.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class DatacatalogProjectsTaxonomiesPatchRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesPatchRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3Taxonomy: A
      GoogleCloudDatacatalogV1alpha3Taxonomy resource to be passed as the
      request body.
    name: Required. Resource name of the taxonomy to be updated.
    updateMask: The update mask applies to the resource. For the `FieldMask`
      definition, see https://developers.google.com/protocol-
      buffers/docs/reference/google.protobuf#fieldmask
  """

  googleCloudDatacatalogV1alpha3Taxonomy = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Taxonomy', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class DatacatalogProjectsTaxonomiesSetIamPolicyRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class DatacatalogProjectsTaxonomiesTestIamPermissionsRequest(_messages.Message):
  r"""A DatacatalogProjectsTaxonomiesTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class Expr(_messages.Message):
  r"""Represents an expression text. Example:      title: "User account
  presence"     description: "Determines whether the request has a user
  account"     expression: "size(request.user) > 0"

  Fields:
    description: An optional description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.  The application context of the containing message
      determines which well-known feature set of CEL is supported.
    location: An optional string indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: An optional title for the expression, i.e. a short string
      describing its purpose. This can be used e.g. in UIs which allow to
      enter the expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class GetIamPolicyRequest(_messages.Message):
  r"""Request message for `GetIamPolicy` method.

  Fields:
    options: OPTIONAL: A `GetPolicyOptions` object for specifying options to
      `GetIamPolicy`. This field is only used by Cloud IAM.
  """

  options = _messages.MessageField('GetPolicyOptions', 1)


class GetPolicyOptions(_messages.Message):
  r"""Encapsulates settings provided to GetIamPolicy.

  Fields:
    requestedPolicyVersion: Optional. The policy format version to be
      returned.  Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected.  Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset.
  """

  requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)


class GoogleCloudDatacatalogV1alpha3AdhocRun(_messages.Message):
  r"""Configuration for ad-hoc runs."""


class GoogleCloudDatacatalogV1alpha3BucketScope(_messages.Message):
  r"""Configuration to scope a crawler to the provided list of buckets.

  Fields:
    buckets: The maximum number of buckets allowed is 1000.
  """

  buckets = _messages.MessageField('GoogleCloudDatacatalogV1alpha3BucketSpec', 1, repeated=True)


class GoogleCloudDatacatalogV1alpha3BucketSpec(_messages.Message):
  r"""Configuration for a crawl bucket.

  Fields:
    bucket: The bucket name. For example, GCS bucket name.
  """

  bucket = _messages.StringField(1)


class GoogleCloudDatacatalogV1alpha3Category(_messages.Message):
  r"""Denotes one category in a taxonomy (e.g. ssn). Categories can be defined
  in a hierarchy. For example, consider the following hierachy:
  Geolocation                    |   ------------------------------------   |
  |                 | LatLong          City              ZipCode Category
  "Geolocation" contains three child categories: "LatLong", "City", and
  "ZipCode".

  Fields:
    childCategoryIds: Output only. Ids of child categories of this category.
    description: Description of the category. The length of the description is
      limited to 2000 bytes when encoded in UTF-8.
    displayName: Required. Human readable name of this category. Max 200 bytes
      when encoded in UTF-8.
    name: Output only. Resource name of the category, whose format is:
      "projects/project_number/taxonomies/{taxonomy_id}/categories/{id}".
    parentCategoryId: Id of the parent category to this category (e.g. for
      category "LatLong" in the example above, this field contains the id of
      category "Geolocation"). If empty, it means this category is a top level
      category (e.g. this field is empty for category "Geolocation" in the
      example above).
  """

  childCategoryIds = _messages.StringField(1, repeated=True)
  description = _messages.StringField(2)
  displayName = _messages.StringField(3)
  name = _messages.StringField(4)
  parentCategoryId = _messages.StringField(5)


class GoogleCloudDatacatalogV1alpha3Crawler(_messages.Message):
  r"""Crawler Metadata.

  Fields:
    config: Required. The configuration of the crawler.
    description: The description of the crawler.
    displayName: Required. The display name of the crawler.
    name: Output only. The resource name of the crawler. Must be empty when
      creating a crawler. For example, "projects/a/crawlers/b".
  """

  config = _messages.MessageField('GoogleCloudDatacatalogV1alpha3CrawlerConfig', 1)
  description = _messages.StringField(2)
  displayName = _messages.StringField(3)
  name = _messages.StringField(4)


class GoogleCloudDatacatalogV1alpha3CrawlerConfig(_messages.Message):
  r"""Crawler configuration.

  Fields:
    adHocRun: Ad-hoc option. User can choose this option for ad-hoc runs.
    bucketScope: Bucket scope. Directs the crawler to crawl specific buckets
      within the project that owns the crawler.
    bundleSpecs: The bundling specifications. Directs the crawler to bundle
      files into filesets based on the bundling specifications.
    organizationScope: Organization scope. Directs the crawler to crawl the
      buckets of the projects in the organization that owns the crawler.
    projectScope: Project scope. Directs the crawler to crawl the buckets of
      the project that owns the crawler.
    scheduledRun: Scheduled option. User can choose this option for scheduled
      runs.
  """

  adHocRun = _messages.MessageField('GoogleCloudDatacatalogV1alpha3AdhocRun', 1)
  bucketScope = _messages.MessageField('GoogleCloudDatacatalogV1alpha3BucketScope', 2)
  bundleSpecs = _messages.StringField(3, repeated=True)
  organizationScope = _messages.MessageField('GoogleCloudDatacatalogV1alpha3ParentOrganizationScope', 4)
  projectScope = _messages.MessageField('GoogleCloudDatacatalogV1alpha3ParentProjectScope', 5)
  scheduledRun = _messages.MessageField('GoogleCloudDatacatalogV1alpha3ScheduledRun', 6)


class GoogleCloudDatacatalogV1alpha3CrawlerRun(_messages.Message):
  r"""A run of the crawler.

  Enums:
    RunOptionValueValuesEnum:
    StateValueValuesEnum: Output only. The state of the crawler run.

  Fields:
    error: Output only. The error status of the crawler run. This field will
      be populated only if the crawler run state is FAILED.
    name: Output only. The name of the crawler run. For example,
      "projects/project1/crawlers/crawler1/crawlerRuns/042423713e9a"
    runOption: A RunOptionValueValuesEnum attribute.
    state: Output only. The state of the crawler run.
  """

  class RunOptionValueValuesEnum(_messages.Enum):
    r"""RunOptionValueValuesEnum enum type.

    Values:
      RUN_OPTION_UNSPECIFIED: Unspecified run option.
      AD_HOC: Ad-hoc run option.
      SCHEDULED: Scheduled run option.
    """
    RUN_OPTION_UNSPECIFIED = 0
    AD_HOC = 1
    SCHEDULED = 2

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The state of the crawler run.

    Values:
      STATE_UNSPECIFIED: Unspecified crawler run state.
      PENDING: This crawler run is waiting on resources to be ready.
      RUNNING: This crawler run is running.
      FAILED: This crawler run failed.
      SUCCEEDED: This crawler run succeeded.
    """
    STATE_UNSPECIFIED = 0
    PENDING = 1
    RUNNING = 2
    FAILED = 3
    SUCCEEDED = 4

  error = _messages.MessageField('Status', 1)
  name = _messages.StringField(2)
  runOption = _messages.EnumField('RunOptionValueValuesEnum', 3)
  state = _messages.EnumField('StateValueValuesEnum', 4)


class GoogleCloudDatacatalogV1alpha3ExportTaxonomiesResponse(_messages.Message):
  r"""Response message for "CategoryManagerSerialization.ExportTaxonomies".

  Fields:
    taxonomies: Required. List of taxonomies and categories in a tree
      structure.
  """

  taxonomies = _messages.MessageField('GoogleCloudDatacatalogV1alpha3SerializedTaxonomy', 1, repeated=True)


class GoogleCloudDatacatalogV1alpha3ImportTaxonomiesRequest(_messages.Message):
  r"""Request message for "CategoryManagerSerialization.ImportTaxonomies".

  Fields:
    taxonomies: Required. Taxonomies to be imported in a tree structure.
  """

  taxonomies = _messages.MessageField('GoogleCloudDatacatalogV1alpha3SerializedTaxonomy', 1, repeated=True)


class GoogleCloudDatacatalogV1alpha3ImportTaxonomiesResponse(_messages.Message):
  r"""Response message for "CategoryManagerSerialization.ImportTaxonomies".

  Fields:
    taxonomies: Required. Taxonomies that were imported.
  """

  taxonomies = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Taxonomy', 1, repeated=True)


class GoogleCloudDatacatalogV1alpha3ListCategoriesResponse(_messages.Message):
  r"""Response message for "CategoryManager.ListCategories".

  Fields:
    categories: Categories that are in this taxonomy.
    nextPageToken: Token to retrieve the next page of results, or empty if
      there are no more results in the list.
  """

  categories = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Category', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudDatacatalogV1alpha3ListCrawlerRunsResponse(_messages.Message):
  r"""Response to listing the runs from a crawler.

  Fields:
    crawlerRuns: The crawler runs from this crawler, it includes both
      currently running and completed runs.
    nextPageToken: Token to retrieve the next page of results or empty if
      there are no more results in the list.
  """

  crawlerRuns = _messages.MessageField('GoogleCloudDatacatalogV1alpha3CrawlerRun', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudDatacatalogV1alpha3ListCrawlersResponse(_messages.Message):
  r"""Response message for `ListCrawlers` API.

  Fields:
    crawlers: List of crawlers.
    nextPageToken: Token to retrieve the next page of results or empty if
      there are no more results in the list.
  """

  crawlers = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Crawler', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudDatacatalogV1alpha3ListTaxonomiesResponse(_messages.Message):
  r"""Response message for "CategoryManager.ListTaxonomies".

  Fields:
    nextPageToken: Token to retrieve the next page of results, or empty if
      there are no more results in the list.
    taxonomies: Taxonomies that the project contains.
  """

  nextPageToken = _messages.StringField(1)
  taxonomies = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Taxonomy', 2, repeated=True)


class GoogleCloudDatacatalogV1alpha3ParentOrganizationScope(_messages.Message):
  r"""Configuration to scope a crawler to the parent Organization."""


class GoogleCloudDatacatalogV1alpha3ParentProjectScope(_messages.Message):
  r"""Configuration to scope a crawler to the parent project."""


class GoogleCloudDatacatalogV1alpha3RunCrawlerRequest(_messages.Message):
  r"""Request to run a crawler manually."""


class GoogleCloudDatacatalogV1alpha3ScheduledRun(_messages.Message):
  r"""Configuration for scheduled runs.

  Enums:
    ScheduledRunOptionValueValuesEnum: Required. The scheduled run option of
      the crawler.

  Fields:
    scheduledRunOption: Required. The scheduled run option of the crawler.
  """

  class ScheduledRunOptionValueValuesEnum(_messages.Enum):
    r"""Required. The scheduled run option of the crawler.

    Values:
      SCHEDULED_RUN_OPTION_UNSPECIFIED: Unspecified scheduled run option.
      DAILY: Daily scheduled run option.
      WEEKLY: Weekly scheduled run option.
    """
    SCHEDULED_RUN_OPTION_UNSPECIFIED = 0
    DAILY = 1
    WEEKLY = 2

  scheduledRunOption = _messages.EnumField('ScheduledRunOptionValueValuesEnum', 1)


class GoogleCloudDatacatalogV1alpha3SerializedCategory(_messages.Message):
  r"""Message representing one category when exported as a nested proto.

  Fields:
    childCategories: Children of the category if any.
    description: Description of the category. The length of the description is
      limited to 2000 bytes when encoded in UTF-8.
    displayName: Required. Display name of the category. Max 200 bytes when
      encoded in UTF-8.
  """

  childCategories = _messages.MessageField('GoogleCloudDatacatalogV1alpha3SerializedCategory', 1, repeated=True)
  description = _messages.StringField(2)
  displayName = _messages.StringField(3)


class GoogleCloudDatacatalogV1alpha3SerializedTaxonomy(_messages.Message):
  r"""Message capturing a taxonomy and its category hierachy as a nested
  proto. Used for taxonomy import/export and mutation.

  Fields:
    categories: Top level categories associated with the taxonomy if any.
    description: Description of the taxonomy. The length of the description is
      limited to 2000 bytes when encoded in UTF-8.
    displayName: Required. Display name of the taxonomy. Max 200 bytes when
      encoded in UTF-8.
  """

  categories = _messages.MessageField('GoogleCloudDatacatalogV1alpha3SerializedCategory', 1, repeated=True)
  description = _messages.StringField(2)
  displayName = _messages.StringField(3)


class GoogleCloudDatacatalogV1alpha3Taxonomy(_messages.Message):
  r"""A taxonomy is a collection of categories of business significance,
  typically associated with the substance of the category (e.g. credit card,
  SSN), or how it is used (e.g. account name, user ID).

  Fields:
    description: Description of the taxonomy. The length of the description is
      limited to 2000 bytes when encoded in UTF-8.
    displayName: Required. Human readable name of this taxonomy. Max 200 bytes
      when encoded in UTF-8.
    name: Output only. Resource name of the taxonomy, whose format is:
      "projects/project_number/taxonomies/{id}".
  """

  description = _messages.StringField(1)
  displayName = _messages.StringField(2)
  name = _messages.StringField(3)


class Policy(_messages.Message):
  r"""Defines an Identity and Access Management (IAM) policy. It is used to
  specify access control policies for Cloud Platform resources.   A `Policy`
  is a collection of `bindings`. A `binding` binds one or more `members` to a
  single `role`. Members can be user accounts, service accounts, Google
  groups, and domains (such as G Suite). A `role` is a named list of
  permissions (defined by IAM or configured by users). A `binding` can
  optionally specify a `condition`, which is a logic expression that further
  constrains the role binding based on attributes about the request and/or
  target resource.  **JSON Example**      {       "bindings": [         {
  "role": "roles/resourcemanager.organizationAdmin",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-project-
  id@appspot.gserviceaccount.com"           ]         },         {
  "role": "roles/resourcemanager.organizationViewer",           "members":
  ["user:eve@example.com"],           "condition": {             "title":
  "expirable access",             "description": "Does not grant access after
  Sep 2020",             "expression": "request.time <
  timestamp('2020-10-01T00:00:00.000Z')",           }         }       ]     }
  **YAML Example**      bindings:     - members:       - user:mike@example.com
  - group:admins@example.com       - domain:google.com       - serviceAccount
  :my-project-id@appspot.gserviceaccount.com       role:
  roles/resourcemanager.organizationAdmin     - members:       -
  user:eve@example.com       role: roles/resourcemanager.organizationViewer
  condition:         title: expirable access         description: Does not
  grant access after Sep 2020         expression: request.time <
  timestamp('2020-10-01T00:00:00.000Z')  For a description of IAM and its
  features, see the [IAM developer's
  guide](https://cloud.google.com/iam/docs).

  Fields:
    bindings: Associates a list of `members` to a `role`. Optionally may
      specify a `condition` that determines when binding is in effect.
      `bindings` with no members will result in an error.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  If no `etag` is provided in the call to `setIamPolicy`, then
      the existing policy is overwritten. Due to blind-set semantics of an
      etag-less policy, 'setIamPolicy' will not fail even if either of
      incoming or stored policy does not meet the version requirements.
    version: Specifies the format of the policy.  Valid values are 0, 1, and
      3. Requests specifying an invalid value will be rejected.  Operations
      affecting conditional bindings must specify version 3. This can be
      either setting a conditional policy, modifying a conditional binding, or
      removing a conditional binding from the stored conditional policy.
      Operations on non-conditional policies may specify any valid value or
      leave the field unset.  If no etag is provided in the call to
      `setIamPolicy`, any version compliance checks on the incoming and/or
      stored policy is skipped.
  """

  bindings = _messages.MessageField('Binding', 1, repeated=True)
  etag = _messages.BytesField(2)
  version = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
  """

  policy = _messages.MessageField('Policy', 1)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class TestIamPermissionsRequest(_messages.Message):
  r"""Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  r"""Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
