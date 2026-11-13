from drafter import *
from dataclasses import dataclass
from Final_Movies import Movie, get_movies


set_website_style("water")
#I used AI to help improve the appearance of my movie recommendation website. Built in dark theme.

@dataclass
class State:
# Store information about the website
    movies: list[Movie]
    selected_genre: str
    minimum_rating: float
    recommended_title: str
    seen_movies: list[str]
    selected_services: list[str]


def card(*content):
    """
    Creates a styled card to organize content on the website.

    AI Assistance: ChatGPT helped me create this function to improve
    the website's appearance without repeating styling code.
    """
    return Div(*content,
               style_background_color="#20232b",
               style_border="1px solid #393e49",
               style_border_radius="14px",
               style_padding="24px",
               style_margin="18px 0")


def movie_heading(title):
    """
    Creates a consistent heading for the website.

    AI Assistance: ChatGPT helped me create this function to
    improve the appearance of headings throughout my website.
    """
    return Header(title, style_color="#f5f5f5",
                  style_font_size="34px")


def red_button(label, destination):
    """
    Creates a red button with consistent styling.

    AI Assistance: ChatGPT helped me create this function to
    improve the appearance of buttons throughout my website.
    """
    return Button(label, destination,
                  style_background_color="#e50914",
                  style_color="white",
                  style_border="none",
                  style_border_radius="8px",
                  style_padding="12px 20px",
                  style_margin="8px 8px 8px 0")


def nav_button(label, destination):
    """
    Creates a consistently styled navigation button.

    AI Assistance: ChatGPT helped me create this function to
    improve the appearance and consistency of navigation buttons.
    """
    return Button(label, destination,
                  style_border_radius="8px",
                  style_padding="10px 16px",
                  style_margin="8px 8px 8px 0")


# Homepage
@route
def index(state: State) -> Page:
    """
    Creates the homepage of my movie recommendation website.

    AI Assistance: ChatGPT helped me improve the layout and
    appearance of the homepage while keeping its functionality.
    """
    return Page(state, [
        Text("THE MOVIE FINDER", style_color="#ff555f",
             style_font_size="16px"),
        card(
            movie_heading("Your next favorite movie starts here."),
            Text("Too many movies, not enough time? Find a movie you'll love based on genre, IMDb rating, and your streaming services.",
                 style_font_size="19px"),
            red_button("Find a Movie", "filter_page")
        ),
        card(
            Header("How it works", style_color="#f5f5f5"),
            Text("1. Choose your favorite genre (or any genre)."),
            Text("2. Set a minimum IMDb rating and pick your streaming services."),
            Text("3. Get a recommendation. Already watched it? See the next one!")
        )
    ])


# Movie filter page
@route
def filter_page(state: State) -> Page:
    """
    Creates the page where users select their movie preferences.

AI Assistance: ChatGPT helped me improve the layout and
    appearance of this page while keeping the filtering
    functionality the same.
    """
    return Page(state, [
        Text("THE MOVIE FINDER", style_color="#ff555f"),
        movie_heading("Choose Your Movie Preferences"),
        card(
            Header("1. Genre"),
            Text("Choose a genre:"),
            SelectBox("genre", [
                "Any Genre", "Action", "Comedy", "Horror", "Sci-Fi", "Drama", "Thriller"
            ], state.selected_genre),
            Header("2. IMDb Rating"),
            Text("Enter your minimum IMDb rating (0-10):"),
            TextBox("rating", state.minimum_rating, "number"),
            Text("Enter 0 for any rating.", style_color="#aeb3bd")
        ),
        card(
            Header("3. Streaming Services"),
            Text("Select any number of services. Leave all boxes unchecked for no preference."),
            RelatedCheckBox("services", "Netflix", "Netflix" in state.selected_services),
            Text("Netflix"),
            RelatedCheckBox("services", "Hulu", "Hulu" in state.selected_services),
            Text("Hulu"),
            RelatedCheckBox("services", "Disney+", "Disney+" in state.selected_services),
            Text("Disney+"),
            RelatedCheckBox("services", "Max (HBO Max)", "Max (HBO Max)" in state.selected_services),
            Text("Max (HBO Max)"),
            RelatedCheckBox("services", "Amazon Prime Video", "Amazon Prime Video" in state.selected_services),
            Text("Amazon Prime Video"),
            RelatedCheckBox("services", "Paramount+", "Paramount+" in state.selected_services),
            Text("Paramount+"),
            RelatedCheckBox("services", "Peacock", "Peacock" in state.selected_services),
            Text("Peacock"),
            RelatedCheckBox("services", "Apple TV", "Apple TV" in state.selected_services),
            Text("Apple TV"),
            RelatedCheckBox("services", "Tubi (Free)", "Tubi (Free)" in state.selected_services),
            Text("Tubi (Free)"),
            RelatedCheckBox("services", "AMC+", "AMC+" in state.selected_services),
            Text("AMC+")
        ),
        red_button("Save Preferences", "save_filters"),
        nav_button("Back to Home", "index")
    ])


# Save the user's preferences
@route
def save_filters(state: State, genre: str, rating: float, services: list[str]) -> Page:
    """
    Saves the user's movie preferences and displays a summary.

    AI Assistance: ChatGPT helped me improve the appearance
    and organization of this page while keeping its original
    functionality.
    """
    state.selected_genre = genre
    state.minimum_rating = rating
    state.selected_services = services
    state.recommended_title = ""

    service_text = ", ".join(state.selected_services)
    if service_text == "":
        service_text = "No preference"

    return Page(state, [
        Text("THE MOVIE FINDER", style_color="#ff555f"),
        movie_heading("Preferences Saved!"),
        card(
            Header("Your selections"),
            Text("GENRE", style_color="#ff555f"),
            Text(state.selected_genre, style_font_size="20px"),
            Text("MINIMUM IMDb RATING", style_color="#ff555f"),
            Text(str(state.minimum_rating) + "/10", style_font_size="20px"),
            Text("STREAMING SERVICES", style_color="#ff555f"),
            Text(service_text, style_font_size="20px")
        ),
        red_button("Get Recommendation", "recommend"),
        nav_button("Change Preferences", "filter_page"),
        nav_button("Back to Home", "index")
    ])


# Find the highest-rated matching movie
@route
def recommend(state: State) -> Page:
    """
    Finds the highest-rated movie that matches the user's preferences.

    AI Assistance: ChatGPT helped me develop and organize the
    recommendation logic using loops and conditional statements.
    """
    best_rating = 0.0
    state.recommended_title = ""

    for movie in state.movies:
        genre_match = False
        if state.selected_genre == "Any Genre":
            genre_match = True
        elif movie.genre.lower() == state.selected_genre.lower():
            genre_match = True

        rating_match = False
        if state.minimum_rating == 0:
            rating_match = True
        elif movie.rating >= state.minimum_rating:
            rating_match = True

        service_match = False
        if len(state.selected_services) == 0:
            service_match = True
        else:
            for service in movie.streaming_services:
                if service in state.selected_services:
                    service_match = True

        if genre_match and rating_match and service_match:
            if movie.title not in state.seen_movies:
                if movie.rating > best_rating:
                    best_rating = movie.rating
                    state.recommended_title = movie.title

    return results(state)


@route
def already_seen(state: State) -> Page:
    """
    Allows users to skip a movie they have already watched.
    """
    state.seen_movies.append(state.recommended_title)
    return recommend(state)


# Display the recommendation
@route
def results(state: State) -> Page:
    """
    Displays the recommended movie or a message if no movies match.

    AI Assistance: ChatGPT helped me improve the layout and
    appearance of the results page while keeping its functionality.
    """
    if state.recommended_title == "":
        return Page(state, [
            Text("THE MOVIE FINDER", style_color="#ff555f"),
            card(
                movie_heading("No Movies Found"),
                Text("No more movies match your preferences.")
            ),
            red_button("Change Filters", "filter_page"),
            nav_button("Back to Home", "index")
        ])

    return Page(state, [
        Text("THE MOVIE FINDER", style_color="#ff555f"),
        movie_heading("Your Movie Recommendation"),
        card(
            Text("TONIGHT'S PICK", style_color="#ff555f",
                 style_font_size="15px"),
            Header(state.recommended_title, style_font_size="32px",
                   style_color="white"),
            Text("Explore the movie details or skip to the next match.",
                 style_color="#c3c6cf"),
            red_button("View Movie Details", "movie_details"),
            nav_button("I've Already Seen This", "already_seen")
        ),
        nav_button("Change Filters", "filter_page"),
        nav_button("Back to Home", "index")
    ])


# Display information about the recommended movie
@route
def movie_details(state: State) -> Page:
    """
    Displays detailed information about the recommended movie.

    AI Assistance: ChatGPT helped me improve the layout and styling
    of this page and implement the IMDb linking feature.
    """
    for movie in state.movies:
        if movie.title == state.recommended_title:
            services = ", ".join(movie.streaming_services)
            if services == "":
                services = "No streaming services listed"

            if movie.imdb_id != "":
                imdb_link = "https://www.imdb.com/title/" + movie.imdb_id + "/"
            else:
                imdb_link = "https://www.imdb.com/find/?q=" + movie.title.replace(" ", "+")

            return Page(state, [
                Text("THE MOVIE FINDER", style_color="#ff555f"),
                movie_heading("Movie Details"),
                card(
                    Header(movie.title, style_font_size="32px",
                           style_color="white"),
                    Text("GENRE", style_color="#ff555f"),
                    Text(movie.genre, style_font_size="21px"),
                    Text("IMDb RATING", style_color="#ff555f"),
                    Text("★ " + str(movie.rating) + "/10",
                         style_font_size="25px", style_color="#ffd166"),
                    Text("WHERE TO WATCH", style_color="#ff555f"),
                    Text(services, style_font_size="18px"),
                    Link("View on IMDb", imdb_link, external=True)
                ),
                red_button("Back to Recommendation", "results"),
                nav_button("I've Already Seen This", "already_seen"),
                nav_button("Back to Home", "index")
            ])

    return Page(state, [
        movie_heading("Movie Not Found"),
        nav_button("Back to Home", "index")
    ])


# Start the website
start_server(State(get_movies(), "Any Genre", 0.0, "", [], []))
