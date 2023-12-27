# Geometry

Planned route in the selected format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FeatureType**](FeatureType.md) |  | 
**geometry** | [**GeoJSONLineString**](GeoJSONLineString.md) |  | 
**properties** | **object** |  | [optional] 

## Example

```python
from mapy_cz_routing.models.geometry import Geometry

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry from a JSON string
geometry_instance = Geometry.from_json(json)
# print the JSON string representation of the object
print Geometry.to_json()

# convert the object into a dict
geometry_dict = geometry_instance.to_dict()
# create an instance of Geometry from a dict
geometry_form_dict = geometry.from_dict(geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


