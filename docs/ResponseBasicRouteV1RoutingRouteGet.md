# ResponseBasicRouteV1RoutingRouteGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **object** |  | [optional] 
**duration** | **object** |  | [optional] 
**geometry** | [**Geometry**](Geometry.md) |  | [optional] 
**detail** | **object** |  | [optional] 

## Example

```python
from mapy_cz_routing.models.response_basic_route_v1_routing_route_get import ResponseBasicRouteV1RoutingRouteGet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBasicRouteV1RoutingRouteGet from a JSON string
response_basic_route_v1_routing_route_get_instance = ResponseBasicRouteV1RoutingRouteGet.from_json(json)
# print the JSON string representation of the object
print ResponseBasicRouteV1RoutingRouteGet.to_json()

# convert the object into a dict
response_basic_route_v1_routing_route_get_dict = response_basic_route_v1_routing_route_get_instance.to_dict()
# create an instance of ResponseBasicRouteV1RoutingRouteGet from a dict
response_basic_route_v1_routing_route_get_form_dict = response_basic_route_v1_routing_route_get.from_dict(response_basic_route_v1_routing_route_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


