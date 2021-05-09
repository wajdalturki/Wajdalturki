
#_______________________________ Library and Dataset : ________________________
library(ggplot2)
library(shiny)
library(tidyverse)
library(readr)
library(shinydashboard)# to create a dashboard

happiness <- read_csv("world_happiness21.csv")
happiness[happiness=="Israel"]<-"palestine"

#_______________________________ user interface  :______________________________
ui <- dashboardPage(
  # dashboard title
  dashboardHeader(title = "The World Happiness 2021"),
  
  dashboardSidebar(
    
    selectInput(inputId="cat1",                                                 # First input for 2 plot to specify the region 
                label=h4("Select a Region"),
                # display choices for users to pick from
                choices=c(
                  "Middle East"="Middle East and North Africa",
                  "Sub-Saharan Africa"="Sub-Saharan Africa",
                  "Western Europe"= "Western Europe",
                  "Central and Eastern Europe"="Central and Eastern Europe",
                  "South Asia" = "South Asia",
                  "Southeast Asia"="Southeast Asia",
                  "East Asia"="East Asia",
                  "North America"="North America and ANZ",
                  "Latin America "="Latin America and Caribbean"
                  
                  
                ),selected = "Middle East", selectize = FALSE),
    
    radioButtons(inputId="scale",                                               # Second input for 2 plot to specify the scale 
                 label=h4("Select The Scale "),
                 list(
                   "Healthy life"="Healthy life expectancy",
                   "Generosity"= "Generosity",
                   "Social support" = "Social support",
                   "GDP"="Logged GDP per capita"
                 )),
    
    radioButtons(inputId="all",                                                 #3th input to cheese between Happiest or Saddest
                 label=h4("Select For Plot 3"),
                 list(
                   "Happiest 10 Countries ",
                   "Saddest 10 Countries"
                 )),
    
    uiOutput("userpanel")                                                       # The dynamically-generated user panel
    
  ),
  dashboardBody(
    
      
      # First tab content
      tabItem(
        tabName = "dashboard",
              fluidRow(
                column(
                  box(title = "Cuntry/Scale",                                                 # The box contain the plot output with formatted size 
                      status = "primary",solidHeader = T,width="800",height = "650",
                      plotOutput("plot1",height = "580")
                  ),width=6
               ),
                column( 
                  box(title =  "The Impact Of GDP On The Other Scales",                                                 # The box contain the plot output with formatted size 
                      status = "primary",solidHeader = T,width="700",height = "300",
                      plotOutput("plot2",height ="230")
                        ),width=5
                  ),
               column( 
                 box(title = "Top 10 Countries With Low/High Ladder Scores",                                                 # The box contain the plot output with formatted size 
                     status = "primary",solidHeader = T,width="700",height = "340",
                     plotOutput("plot3",height ="280")
               ),width=5
               )
      )
    )
    ),
)
  
  #___________________________________ server : __________________________________
  
server <- function(input, output) {
    
    #___________________________________ plot 1 : __________________________________ 
    output$plot1 <- renderPlot({
      
      happiness_f <- happiness[happiness$`Regional indicator` == input$cat1,      # Filter the dataset with the user input  
                               c('Country name',input$scale)]
      happiness_f<-as.data.frame(happiness_f)                                                                   
      
      happiness_f %>%
        ggplot(aes(x=reorder(happiness_f[,1],happiness_f[,2]), y=happiness_f[,2]))+# Create the ggplot from the inputs
        geom_bar(stat = 'identity', 
                 fill=ifelse(input$cat1=="Middle East and North Africa","#84A59D",# To change the bar color for every region 
                      ifelse(input$cat1=="Western Europe","#897198", 
                      ifelse(input$cat1=="South Asia","#B56576",
                      ifelse(input$cat1=="Central and Eastern Europe", "#E56B6F",
                      ifelse(input$cat1=="Sub-Saharan Africa","#F29602",
                      ifelse(input$cat1=="Southeast Asia","#BB9457",
                      ifelse(input$cat1=="Latin America and Caribbean","#E6DBB3",
                      ifelse(input$cat1=="North America and ANZ","#BC4B51","#ADC178")
                      )))))))) +
        geom_text(aes(label=happiness_f[,2]),hjust=1.5,color="black",size=5)+     # Print the values in the top of the bar 
        labs(x='Country name', y=input$scale ,size=12)+                           # Add  name to the axis
        coord_flip()+                                                             # Flip the axis 
        theme(                                                                    # Change the color of the axis name and title (x,y) 
          axis.text.y = element_text(face="bold", color="#993333",size=14),     
          axis.text.x = element_text(face="bold", color="#993333",size=14),
          axis.title.x = element_text(color="#993333", size=14, face="bold"),
          axis.title.y = element_text(color="#993333", size=14, face="bold")
        )
      
    })
    #___________________________________ plot 2 : __________________________________ 
    output$plot2 <- renderPlot({
      title2 <- " by Region"
      happiness_f <- happiness[happiness$`Regional indicator` == input$cat1,      # Filter the dataset with the user input
                               c("Logged GDP per capita",input$scale)]
      happiness_f<-as.data.frame(happiness_f)
      
      happiness_f %>%
        ggplot(aes(x=happiness_f[,1], y=happiness_f[,2])) +                       # Create the ggplot from the input
        geom_point(aes(color = happiness_f[,1],size = 3)) +
        scale_color_gradient(low = "#E56B6F", high = "#597CB1")+                  # Generate custom colors 
        geom_smooth(method = "lm")+
        labs(title=title2, x="Logged GDP per capita", y=input$scale)+             # Add name to the axis
        theme(                                                                    # Change the color of the axis name and title (x,y) 
          axis.text.y = element_text(face="bold", color="#993333",size=14),
          axis.text.x = element_text(face="bold", color="#993333",size=14),
          axis.title.x = element_text(color="#993333", size=14, face="bold"),
          axis.title.y = element_text(color="#993333", size=14, face="bold"),
          legend.position = "none"
        )
      
    })
    
    #___________________________________ plot 3 : __________________________________ 
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
            axis.text.x = element_text(face="bold", color="#993333",size=14),
            axis.title.x = element_text(color="#993333", size=14, face="bold"),
            axis.title.y = element_text(color="#993333", size=14, face="bold")
          )
        
      }
      
    })
    
  }
  
  shinyApp(ui, server)
