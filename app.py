#!/usr/bin/env python
# coding: utf-8

# In[22]:


from flask import Flask


# In[23]:


from textblob import TextBlob


# In[24]:


app = Flask(__name__)


# In[25]:


from flask import request, render_template

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        text2analyze = request.form.get("text2analyze")
        print(text2analyze)
        sentiment = TextBlob(text2analyze).sentiment
        return(render_template("index.html", result=sentiment))
    else:
        return(render_template("index.html", result="Loaded"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




