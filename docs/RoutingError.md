# RoutingError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **object** |  | [optional] 
**error_code** | **object** |  | [optional] 

## Example

```python
from mapy_cz_routing.models.routing_error import RoutingError

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingError from a JSON string
routing_error_instance = RoutingError.from_json(json)
# print the JSON string representation of the object
print RoutingError.to_json()

# convert the object into a dict
routing_error_dict = routing_error_instance.to_dict()
# create an instance of RoutingError from a dict
routing_error_form_dict = routing_error.from_dict(routing_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


