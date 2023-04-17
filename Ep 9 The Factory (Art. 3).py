#The Factory
#table formation
form a table consisting of same no. of rows and columns
with same names and in order
mark the cells (according to rows) which instruction depends on which other instructions


#arranging the instructions
l=[]
while no.of rows !=0:
    choose the instruction which does no depend on any other instruction
    i.e. no arrows pointing to it

    write the instruction at theend of the list, l


    delete its row and column from the table
    i.e. remove existence of that instruction from the table

print('List of instructions:',l)
