# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 09:29:40 2021

@author: erkum
"""

import streamlit as st #for web dev

import tensorflow as tf
import gpt_2_simple as gpt2
from datetime import datetime
import os
#from SessionState import _SessionState, _get_session, _get_state
from google.colab import files

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)  


gpt2.mount_gdrive()
#gpt2.copy_checkpoint_from_gdrive()
st.title("GPT2 Web App")

dataset_name = st.sidebar.selectbox("Select Positive Author Novel",("Stephen King","Robert Jordan","Michael Connelly","Laurell K. Hamilton","Terry Goodkind","Jim Butcher","Steven Erikson","Lee Child","Kim Harrison","Stephen R. Donaldson"))

trained_model = st.sidebar.selectbox("Select Trained Model",("LSTM","GPT2"))

if((dataset_name == "Stephen King")  and (trained_model == "GPT2")):
    st.title("Stephen King")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Text Generation using GPT-2/checkpoint_stephen/checkpoint/"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    
    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
         
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)
        
elif((dataset_name == "Robert Jordan")  and (trained_model == "GPT2")):
    st.title("Robert Jordan")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Robert Jordan/checkpoint/"
    checkpoint_dir=os.path.dirname(checkpoint_path)
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    
    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)      

elif((dataset_name == "Michael Connelly")  and (trained_model == "GPT2")):
    st.title("Michael Connelly")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Micheal Colleny/checkpoint/"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    
    #instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)


    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)


elif((dataset_name == "Laurell K. Hamilton")  and (trained_model == "GPT2")):
    st.title("Laurell K. Hamilton")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Laurell k. Hamilton/checkpoint"
    checkpoint_dir=os.path.dirname(checkpoint_path)
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    


    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)
    
elif((dataset_name == "Terry Goodkind")  and (trained_model == "GPT2")):
    st.title("Terry Goodkind")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Terry Goodkind/checkpoint"
    checkpoint_dir=os.path.dirname(checkpoint_path)
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    


    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)
    
elif((dataset_name == "Jim Butcher")  and (trained_model == "GPT2")):
    st.title("Jim Butcher")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Jim Butcher/checkpoint"
    checkpoint_dir=os.path.dirname(checkpoint_path)
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    


    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)
    
elif((dataset_name == "Steven Erikson")  and (trained_model == "GPT2")):
    st.title("Steven Erikson")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Steven Erikson/checkpoint"
    checkpoint_dir=os.path.dirname(checkpoint_path)
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    


    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)
    
elif((dataset_name == "Lee Child")  and (trained_model == "GPT2")):
    st.title("Lee Child")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Lee Child/checkpoint"
    checkpoint_dir=os.path.dirname(checkpoint_path)
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    


    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)
    
elif((dataset_name == "Kim Harrison")  and (trained_model == "GPT2")):
    st.title("Kim Harrison")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Kim Harrison/checkpoint"
    checkpoint_dir=os.path.dirname(checkpoint_path)
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    


    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)
    
elif((dataset_name == "Stephen R. Donaldson")  and (trained_model == "GPT2")):
    st.title("Stephen R. Donaldson")
    checkpoint_path = "/content/drive/MyDrive/Project folder/Author wise text generation using GPT/Stephen R. Donaldson_cleaned/checkpoint"
    checkpoint_dir=os.path.dirname(checkpoint_path)
    # instantiate the model / download
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,checkpoint_dir=checkpoint_path)
    


    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "This generator predict about")
    
    
    with st.spinner("AI is at Work........"):
        # text generation
         gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())
    
         gpt2.generate_to_file(sess,
                          checkpoint_dir=checkpoint_path,
                          prefix=prompt_text,
                          destination_path=gen_file,
                          length=500,
                          temperature=1,
                          nsamples=1,
                          batch_size=1
                          )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    file=open(gen_file)
    text=file.read()
    print('Corpus length in characters=', len(text))        
    print((text).encode('utf8')) 
    st.markdown(text)
else:
    st.title("IN PROCESSING")