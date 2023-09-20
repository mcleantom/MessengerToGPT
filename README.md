# MessengerToGPT
Convert your facebook messenger messages into a GPT model.


Instructions:

1. Download your facebook messages (follow [this](https://www.remote.tools/remote-work/download-facebook-messenger-conversation) tutorial)

2. Create a new conda environment:

```
conda create -n MessengerToGPT python==3.10
```

3. Activate the new environment:
```
conda activate MessengerToGPT
```

4. Install the requirements (the only requirement is torch):
```
pip install -r requirements.txt
```

5. Convert your facebook messages into the correct format.

Within `convert_messages_into_chat_format.py` change the root_folder to the facebook message folder you want to train off.
Then run:

```
python convert_messages_into_chat_format.py
```

6. Train the model and run it.

First, go into `model.py` and change the `message_file` variable to the value of `output_file` in `convert_messages_into_chat_format.py`.
Also change `initial_message` to whatever you want the initial seed to be. Then, run: 
```
python model.py
```
Example output:

```
Cameron Owens:
Eat sleep meme repeat

Tom McLean:
Trying to find my meme stash

Cameron Owens:
😂😂😂😂

Cameron Owens:
Memes are my high

Cameron Owens:
Church

Tom McLean:
Top meme

Cameron Owens:
I'm in love with the coco

Tom McLean:
Do you have the data from the S2 lab?

Cameron Owens:
I might

Cameron Owens:
Will need memes in exchange though

Cameron Owens:
And they better be really ironic

Tom McLean:
I have some pretty dank ones

Tom McLean:
Deal.
```
