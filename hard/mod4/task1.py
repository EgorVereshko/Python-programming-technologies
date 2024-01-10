import json

string = "description: input. exAMPLE; salary: 7.3535353535; key_skills: Example&nbspKey&nbspSkills;"
dictionary = "description, salary"

input_data = string.split("; ")
data_dict = {}
for elem in input_data:
    key, value = elem.split(": ")
    data_dict[key] = value

for elem in dictionary.split(", "):
    if elem in data_dict:
        if elem == "description":
            sentences = data_dict[elem].split(". ")
            processed_sentences = [sentence.capitalize() for sentence in sentences]
            data_dict[elem] = ". ".join(processed_sentences)

        if elem == "salary":
            salary_value = float(data_dict[elem])
            rounded_salary = round(salary_value, 3)
            data_dict[elem] = "{:.3f}".format(rounded_salary)

        if elem == "key_skills":
            data_dict[elem] = data_dict[elem].replace("&nbsp", " ")

result = json.dumps(data_dict)
print(result)
