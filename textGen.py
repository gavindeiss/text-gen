import markovify
import json

# # Get raw text as string.
# with open("corpus.txt") as f:
#     text = f.read()

# # Build the model.
# text_model = markovify.Text(text)

# # Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence())
#     print("\n")

# print("==================")

# # Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))
#     print("\n")

 
files = ['lotr.txt', 'murakami.txt']  # dune, harry potter
#files = ['corpus.txt'] 

combinedModel = None
for file in files:
	print(file)
	text = None
	with open(file) as f:
		text = f.read()[:80000]

	model = markovify.Text(text, retain_original=False)
	if combinedModel:
		combinedModel = markovify.combine(models=[combinedModel, model])
	else:
		combinedModel = model

for i in range(20):
	for j in range(3):
		print(combinedModel.make_sentence())
	print('\n')

modelJson = combinedModel.to_json()
with open('modelJson.json', 'w') as outfile:
    outfile.write(modelJson)

# loadedModel = None
# with open('modelJson.json') as json_file:
#     loadedModel = json.load(json_file)
# reconstituted_model = markovify.Text.from_json(loadedModel)
# reconstituted_model.make_sentence()



