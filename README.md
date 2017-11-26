# Should I Watch This?
### **Team JAIMS Smith**
Jennifer Zhang

Alessandro Cartegni

Ibnul Jahan

Michael Ruvinshteyn
___

### Overview
*Should I Watch This?* is an application that provides information about a movie, including titles, reviews, and recommendations. Logging in gives you access tomore features, such as getting your movie recommendations based on your search history.

### Instructions on how to run (Including how to procure API keys.)
1. Open command prompt, and, from there, navigate to the desired directory.
2. Clone the repository:
   * ```git clone https://github.com/jennifer4569/p01.git```
3. Activate your virtual environment.
   * For example, if your virtual environment is called *jaims*:
     * ```source jaims/bin/activate```
     * **Note: Activating virtual environments on different devices may vary**
4. Set up your API Keys:
   * OMDb API
		1. Go to http://www.omdbapi.com/apikey.aspx
		2. Create an account.
		3. Go to the email labeled *OMDb API Key*, and click the bottom link to activate your key.
		4. Copy the first link given, labeled *"OMDb API"*.
		5. Refer to step 5 below. Replace **\<OMDB API URL>** with the link you were given in the last step.
   * NYT API
     	1. Go to https://developer.nytimes.com/signup
     	2. Fill out the form.
     		* For website, it is fine if you put localhost:5000
     		* For API, make sure you select Movie Reviews API 
     	3. Go to the email labeled *Your NYTimes API Key*
     	4. Copy your API key, which is right next to *"Here's your API Key for the Movie Reviews API: "*
     	5. Refer to step 5 below. Replace **\<NYT API Key>** with the key you were given in the last step.
   * TasteDive API
   		1.  Go to https://tastedive.com/account/signin?next=https%3A%2F%2Ftastedive.com%2Fread%2Fapi
   		2.  Create an account
   		3.  Go to https://tastedive.com/account/api_access
	   		* For application name, put "Should I Watch This?"
	   		* For description, put "This app gets movie recommendations."
   		4. Press save, and then copy your API access key.
   		5. Refer to step 5 below. Replace **\<TasteDive API Key>** with the key you were given in the last step
5. Go to api.py, and on the first 3 lines, paste the following:
    ```
   	omdb_url = "<OMDB API URL>"
  	nyt_url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=<NYT API KEY>"
   	tastedive_url = "https://tastedive.com/api/similar?k=<TasteDive API Key>"
    ```
    * Make sure to replace <> with their respective links. (Refer to step 4 for the respective instructions)
    	* For example, if:
    		* The url given for the OMDb API was http://www.omdbapi.com/?i=tt3896198&apikey=asijdfoi
    		* The API key given for the NYT API was 2109380912388uwfjosfd
    		* The API key given for the TasteDive API was 9asdfjkl12038
    	* Then the first 3 lines should look like:
    		```
        	omdb_url = "http://www.omdbapi.com/?i=tt3896198&apikey=asijdfoi"
  			nyt_url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=2109380912388uwfjosfd"
    		tastedive_url = "https://tastedive.com/api/similar?k=9asdfjkl12038"
	        ```
6. Run the program.
   * ```python app.py```