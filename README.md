Story book narrative model

run the program using app.py 

--This model can able to generate it's own story and images --we are accessing pretrained models to this project like (Gemini) -- And leverage the model by using of intel openvino toolkit for optimize the rendering time -- you can't directly access the model because you need the access token key from hugging face.

Technnologies that we are used : LLM: The LLM basically narrte the story from the online of prompt

Stable diffusion: It will generate the images with the help of prompt that is produced by the LLM

SQL: We also having the login page.the user datas are going to story into the local database

Fine Tuning: ! For fine tuning we are using LORA (low rank adaptatioin) which is basically freeze the base parameters and use the lora weights

Flow chart :![flowchart](https://github.com/user-attachments/assets/6fe071a2-68dd-4b1a-a065-e7d39c6f95ab)

--we are giving only one image for inferencing because of it's takes 1 min for each image
