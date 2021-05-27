library(datasets)



# ============================ global variables ================================



movies_adult - c('Wonder Woman', 'Fast And Furious five', 'The Little Things ', 'The King s Man', 'No Time to Die')

movies_children - c('tom and jary', 'Soul', 'Vivo ', 'Luca', 'Minions: The Rise of Gru')  

week_days -c("saturday","sunday","Monday","Tuesday"," Wednesday","Thursday","Friday")



ticket_cost -50

ticket_cost_child -(ticket_cost/2)

screens -2                  

seats -30                      

       

week_revenue_children-c()

week_revenue_adult-c()





# ============================ children_revenue ================================

children_revenue_movies-function(){

 # days loop

 for (i in 1:length(week_days)) {

   name_of_day-week_days[i]

   print(name_of_day)

   total_of_the_day-0

   

   # screen loop

   for(i in 1:screens){  

     if(i=length(movies_children)){

   

     # for every screen create sample adults and children

     visitors_children - sample(1:seats, size=1)

     visitors_adults - sample(1:(seats-visitors_children), size=1)

     

     # calculate the revenue for adults and children

     adult_revenue-visitors_adults*ticket_cost

     children_revenue-visitors_children*ticket_cost_child

     

     

     # sum the revenues for all ticket

     total_of_the_day-sum(adult_revenue,children_revenue,total_of_the_day)

     

     random_movies - sample(1:length(movies_adult), size=1)

     print(paste0("Screen :",i))

     print(paste0("Movie Name :",movies_children[random_movies]))

     print(paste0("number of children  ",visitors_children))

     print(paste0("number of adults  ",visitors_adults))

     print(paste0("total revenue of adults  ",adult_revenue))

     print(paste0("total revenue of cheldren  ",children_revenue))

     }

   }

   

   # print the total of the day

   print(paste0("total   ",total_of_the_day))

   

   print("---------------------------------------------------------------------")

   

   # victor to save the total_of_the_day

   week_revenue_children-c(week_revenue_children,total_of_the_day)

   

 }

 print("###############################################################3")

 # create a data frame  and view it

 df_children-data.frame(week_days,week_revenue_children)

 df_report-df_children[order(-week_revenue_children),]

 View(df_children)

 

 #  bar plot for the data frame

 barplot(

   df_report$week_revenue_children,

   names.arg=df_report$week_days,

   xlab="Days",

   ylab="Revenue",

   col="blue",

   main="cheldren`s movies revenue for the week"

   )

}

children_revenue_movies()



# ============================= adult_revenue =================================

adult_revenue_movies-function(){

 

 # days loop

 for (i in 1:length(week_days)) {

   name_of_day-week_days[i]

   print(name_of_day)

   total_of_the_day-0

   

   # screen loop

   for(i in 1:screens){  

     if(i =length(movies_adult)){  

     # for every screen create sample adults

     visitors_adults - sample(1:seats, size=1)

     

     # calculate the revenue for adults

     adult_revenue-visitors_adults*ticket_cost

     

     # sum the revenues for all ticket

     total_of_the_day-sum(adult_revenue,total_of_the_day)

     

     random_movies - sample(1:length(movies_adult), size=1)

     print(paste0("Screan :",i))

     print(paste0("Movie Name :",movies_adult[random_movies]))

     print(paste0("number of adults  ",visitors_adults))

     print(paste0("total revenue of adults  ",adult_revenue))

     

   }}

   week_revenue_adult-c(week_revenue_adult,total_of_the_day)

   print(paste0("total   ",total_of_the_day))

   print("---------------------------------------------------------------------")

   

 }

 # create a data frame  and view it

 df_adult-data.frame(week_days,week_revenue_adult)

 df_report-df_adult[order(-week_revenue_adult),]

 View(df_adult)

 #  bar plot for the data frame

barplot(

   df_report$week_revenue_adult,

   names.arg=df_report$week_days,

   xlab="Days",

   ylab="Revenue",

   col="red",

   main="adult`s movies revenue for the week"

 )

}

#adult_revenue_movies()




















