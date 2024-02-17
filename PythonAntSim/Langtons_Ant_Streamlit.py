import streamlit as st
import numpy as np

# Creating side bars to control animation
colorRangeChoice = st.sidebar.slider("Color Depth",1,50,5,1)
MatrixN = st.sidebar.slider("DisplayLength",10,100,10,5)
itterations = st.sidebar.slider("Itterations to run",50,1000,5)

# Adding a progress bar to know simulation time
progressBar = st.sidebar.progress(0)

# Instantiate image
frame = st.empty()

# Instantiate grid and ant starting position
grid = np.zeros(MatrixN,MatrixN)
antPos = [MatrixN/2,MatrixN/2,1] #[X Pos, Y Pos, Direction (1:N,2:E,3:S,4:W)]

# Show empty grid
image.image(grid)

# Run for i itterations
#for i in enumerate(np.linspace(0,itterations,1)):

    # Update progress bar
    #progressBar.progress(i)

    # Move Ant & Update Direction

    # Update cell value under ant

    # Update image

# Clear elements by calling empty on them.
progressBar.empty()

# Show rerun button on completion
st.button("Run Again!")