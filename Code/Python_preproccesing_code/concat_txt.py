file_output = "D:\\SynthTalkOne\\output.txt"


with open(file_output, "w") as output_file:
    for i in range(1, 165):
        file_path = f"D:\\00_UNI\\6toSemestre\\MachineLearning\\Project\\SynthTalkOne\\txt\\{i}.txt"  # Replace with the actual file path pattern

        with open(file_path, "r") as input_file:
            content = input_file.read().strip()
            output_file.write(content)
            output_file.write("\n")
print("already finished!")