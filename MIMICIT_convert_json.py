import json
import random
import argparse

def convert_to_output_format(input_data):
    output_list = []

    for key, value in input_data["data"].items():
        conversation = [
            {
                "from": "human",
                "value": f"{value['instruction']}"
            },
            {"from": "gpt", "value": value["answer"]}
        ]

        # 在句首或句尾添加 <image><image>
        conversation[0]["value"] = f"<image>\n{conversation[0]['value']}"

        output_list.append({
            "id": key,
            "image": "|".join([f"images/MIMICIT/LA/{image_id}.jpg" for image_id in value["image_ids"]]),
            "conversations": conversation
        })

    return output_list

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate conversations based on input JSON file.")
    parser.add_argument("input_file", help="Path to the input JSON file")

    args = parser.parse_args()

# 读取输入文件
    with open(args.input_file, "r", encoding="utf-8") as input_file:
        input_data = json.load(input_file)

# 转换格式
    output_data = convert_to_output_format(input_data)

# 输出到文件
    with open("llava_{}".format(args.input_file), "w") as output_file:
        json.dump(output_data, output_file, ensure_ascii=False, indent=2)


