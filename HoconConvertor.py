from pyhocon.tool import HOCONConverter
import yaml
import json
import pyhocon


def yamlConvHocon(filename):
    try:
        with open(filename, 'r') as yaml_in, open("temp.json", "w") as json_out:
            yaml_object = yaml.safe_load(yaml_in)  # yaml_object will be a list or a dict
            json.dump(yaml_object, json_out)
    except FileNotFoundError:
        print("Yaml file not found")
    hoconFileName = filename.replace('yaml',"config")
    with open("temp.json", "r") as jsonDoc, open(hoconFileName, "w") as file_hocon:
        factory = pyhocon.ConfigFactory.parse_string(jsonDoc.readline(), resolve=True)
        file_hocon.write(HOCONConverter().to_hocon(factory))
    return hoconFileName



def HoconConvertorTest(filename):
    hoconFileName=yamlConvHocon(filename)
    HOCONConverter.convert_from_file(hoconFileName, "Test"+filename, 'yaml')
    with open("Test"+filename, 'r') as yaml_in, open(filename, "r") as yaml_out:
        a = yaml_out.read()
        b = yaml_in.read()
        assert a ==b


if __name__ == "__main__":
    #print("Enter file Yaml name and location")
    filename = "value.yaml"  # input()
    yamlConvHocon(filename)
    filename="test.yaml"
    HoconConvertorTest(filename)