import json


def read_ocr_results(path_to_file: str):
    """
    Read OCR results from a JSON file and concatenate all text pieces into a single string.
    """
    try:
        with open(path_to_file, "r") as file:
            data_dict = json.load(file)

        page_content = []
        metadata = []
        first_list = list(data_dict.values())[0]
        file_name = list(data_dict.keys())[0]

        for page_no, element in enumerate(first_list, start=1):
            text_lines = element[list(element.keys())[0]]
            text_pieces = []
            for line in text_lines:
                text_pieces.append(line["text"])
            page_content.append(" ".join(text_pieces))
            metadata.append({"page_no": page_no, "file_name": file_name})
        return page_content, metadata

    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", str(e))
    except FileNotFoundError:
        print("File not found:", path_to_file)
    except Exception as e:
        print("An error occurred:", str(e))


# if __name__ == "__main__":
#     read_ocr_results("data/results/surya/sample2/results.json")
