
library(ggplot2)
library(shiny)
library(tidyverse)
library(readr)
library(shinydashboard)# to create a dashboard

happiness <- read_csv("world_happiness21.csv")
happiness[happiness=="Israel"]<-"palestine"

ui <- dashboardPage(
  # dashboard title
  dashboardHeader(title = "The World Happiness 2021"),
  

_______________________________ 
    output$plot3 <- renderPlot({
      happiness_l <- happiness %>% arrange(desc(`Ladder score`))                  # Arrange the Ladder score descending from the dataset  
      
      if(input$all=="Happiest 10 Countries "){                                    # If the user want the happiest 10 countries
        top10<- head(happiness_l,10)                                              # Take the top 10 rows after the the arrangement 
        ggplot(top10,aes(x=reorder(`Country name`,`Ladder score`),y=`Ladder score`)) +# create the plot 
          geom_bar(stat = 'identity',fill="#B08968") +                            # Bar chart
          ggtitle("Top 10 Countries With High Ladder Scores")+                    # Plot title
          geom_text(aes(label=`Ladder score`),hjust=1.5,color="white",size=5)+    # Print the Ladder score values in the top of the bar
          labs(x='Country name', y='Ladder score' ,size=12)+                      # Add name for the axis
          ylim(0,10)+                                                             # Reset the y axis values
          coord_flip()+                                                           # Flip the axis 
          theme(                                                                  # Change the color of the axis name and title (x,y) 
            axis.text.y = element_text(face="bold", color="#993333",size=14),
            axis.text.x = element_text(face="bold", color="#993333",size=14),
            axis.title.x = element_text(color="#993333", size=14, face="bold"),
            axis.title.y = element_text(color="#993333", size=14, face="bold")
          )
        
      }else{                                                                      #If the user want the happiest 10 countries
        top10<- tail(happiness_l,10)                                              # Take the last 10 rows after the the arrangement
        ggplot(top10,aes(x=reorder(`Country name`,-`Ladder score`), y=`Ladder score`)) +# create the plot 
          geom_bar(stat = 'identity',fill="#EAAC8B") +                            # Bar chart
          ggtitle("Top 10 Countries With Low Ladder Scores")+                     # Plot title
          geom_text(aes(label=`Ladder score`),hjust=1.5,color="white",size=5)+    # Print the Ladder score values in the top of the bar
          labs(x='Country name', y='Ladder score' ,size=12)+                      # Add name for the axis
          ylim(0,10)+                                                             # Reset the y axis values
          coord_flip()+                                                           # Flip the axis 
          theme(                                                                  # Change the color of the axis name and title (x,y) 
            axis.text.y = element_text(face="bold", color="#993333",size=14),
