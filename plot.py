import streamlit as st
import pandas as pd
import re
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
import plotly.graph_objects as go


df = pd.read_csv("Damage.csv")
cols = df.columns


def clean_the_response(response):
    if "```" in response:
        pattern = r'```(.*?)```'
        code = re.search(pattern, response, re.DOTALL)
        if code:
            extracted_code = code.group(1)
            extracted_code = extracted_code.replace('python', '').strip()
            return extracted_code
    return response.strip()


def create_plot(user_input, cols):
    
    human_message = HumanMessagePromptTemplate.from_template(
        "Write code in Python using Plotly to address the following request: {user_input}. "
        "Use a dataframe `df` that has the following columns: {cols}. "
        "Do not use the `animation_group` argument and return only code with no import statements. "
        "Assume the data has already been loaded into a variable `df`."
    )
    prompt_template = ChatPromptTemplate(messages=[human_message])
    
    
    chat_model = Ollama(model="gemma2:2b")  
    chain = LLMChain(llm=chat_model, prompt=prompt_template)
    
    
    response = chain.run({"user_input": user_input, "cols": list(cols)})
    extracted_code = clean_the_response(response)
    
    
    try:
        
        local_scope = {'go': go, 'df': df}  
        exec(extracted_code, {}, local_scope)
        fig = local_scope.get('fig')  
        return fig  
    except Exception as e:
        return f"Error executing code: {e}"


def main():
    st.title("Interactive Vehicle Distribution Plotter")

    
    user_input = st.text_input("Enter the graph description", "Show a graph with distribution of vehicles across each fleet")
    
    
    if st.button("Generate Plot"):
        
        plot = create_plot(user_input, cols)
        
        if isinstance(plot, str):  
            st.error(plot)
        else:
            st.plotly_chart(plot)


if __name__ == "__main__":
    main()
