    #     This is some information that will propably help you to answer the following question. 
    # You need to process it but if its unrelated just ignore it!
    # {cont}

PROMPT_TEMPLATE = """

    ----
    On the provided table below.
    You need to examine carefully the table and provide the relations between the columns of the table!
    ----
    All the possible relations are in this list {distinct_values}.
    Examine all the possible provided realtioins and keep the most suitable one!
    Be carefull to only use the list of relations!
    ----
    Example 
    Given this table:
    |col0|col1|col2|
    |Greece|131.957|10.413.982|
    |Malta|316|542.051|

    Desired output
    |col|relation|col|
    |col0|area|col1|
    |col0|population|col2|
    ----
    Now do this with this table  
    Provide only the desired output and nothing more! Dont explain yourself and dont provide extra comments!
    ---

    {table}

    ---

    """
PROMPT_TEMPLATE_STRUCTURING = """ 
--
Desired format:
|col|relation|col|
|col0|Founded_by|col1|
|col0|Founded_in|col2|
--
Is the following in the format i want?
{res}
--
If not make it!  
Make sure to provide only the Desired format and nothing more!

"""

PROMPT_TEMPLATE_TYPO= """
{text}
Is there any typo? provide only the correct version nothing more!
for example 
-input: wikpedia
-desired output: wikipedia 
"""