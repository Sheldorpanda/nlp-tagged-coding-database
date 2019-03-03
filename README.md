Hackathon project for Hoohacks, March 2-3 2019.

## Inspiration

As first year and second year computer science students, we would like to find great programming projects to work on for educational purposes and to build our resume. Some websites, such as GitHub, tag projects to make them easily identified. However, the tags mostly depend on the project owner, and some important information are not shown as tags, such as how hard the project is, and will it fit the student's level. We believe some useful, descriptive information is hidden in the project documents and we should be able to mine it out.

## What it does

It first uses a natural language processing AI to process all documents in a GitHub repository. After giving some tags such as "level", "legit" and "popularity", the tagged data is fed into a Django application, which is a new search engine of coding projects by those tags.

## How I built it

We wrote a Beautifulsoup4 web scrapper to recursively go into GitHub directories and scrap all natural language-written documents (.md, .rst and .txt) from GitHub repositories, and manually labelled the tags for the training data. The labelled data is given to a Tensorflow Keras deep neural network to do NLP training. After the network converges, it is used to predict tags on larger data. 

We then built a Django application as a GitHub project dashboard with search function based on the tags. It is deployed on AWS cloud server.

## Challenges I ran into

Some of the tags, such as the difficulty level of a project, have no reference. Hence we need to evaluate them very carefully when labeling the training data. Also, Tensorflow-gpu requires large computational power, so we used [the GPU servers provided by University of Virginia](http://www.cs.virginia.edu/wiki/doku.php?id=compute_resources).

## Accomplishments that I'm proud of

We are actually surprised that the training and validation loss converges. Although the final accuracy is not good (approximately 0.6), we believe it is due to the fact that we are lacking of a rigorous labeling method, and the training data size is small (100 GitHub repos). We believe we are on the right track to mine hidden features out of coding project documents. Also, we are proud of being able to figure out the html architecture of GitHub repositories and successfully scrap the data.

## What I learned

NLP APIs in Tensorflow Keras, as well as developing both the front end and back end of a Django project.

## What's next for NLP-tagged Coding Project Database

If feasible, we shall make a more rigorous labeling method and better defined categories, and present our tags along with existing tags such as those given by GitHub. The NLP will be run on a larger data as well. We would also like to make this technique expand to more coding project websites other than GitHub, to make computer science students access available projects as many as possible. Furthermore, we can make our Django website look better.
