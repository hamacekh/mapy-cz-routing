# RoutingErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **object** |  | [optional] 

## Example

```python
from mapy_cz_routing.models.routing_error_response import RoutingErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingErrorResponse from a JSON string
routing_error_response_instance = RoutingErrorResponse.from_json(json)
# print the JSON string representation of the object
print RoutingErrorResponse.to_json()

# convert the object into a dict
routing_error_response_dict = routing_error_response_instance.to_dict()
# create an instance of RoutingErrorResponse from a dict
routing_error_response_form_dict = routing_error_response.from_dict(routing_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


