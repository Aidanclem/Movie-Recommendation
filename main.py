from drafter import *
from dataclasses import dataclass
from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    genre: str
    rating: float
    favorite: bool
    streaming_services: list[str]
    imdb_id: str = ""


def get_movies() -> list[Movie]:
    return [
Movie('12 Strong', 'Action', 6.5, False, ['Peacock'], 'tt1413492'),
        Movie('13 Hours: The Secret Soldiers of Benghazi', 'Action', 7.3, False, ['Paramount+', 'Peacock'], 'tt4172430'),
        Movie('2 Fast 2 Furious', 'Action', 5.9, False, ['Peacock'], 'tt0322259'),
        Movie('3 Days to Kill', 'Action', 6.2, False, ['Max (HBO Max)'], 'tt2172934'),
        Movie('48 Hrs.', 'Action', 6.9, False, ['Paramount+'], 'tt0083511'),
        Movie('Air Force One', 'Action', 6.5, False, ['Netflix', 'Peacock'], 'tt0118571'),
        Movie('American Made', 'Action', 7.1, False, ['Amazon Prime Video'], 'tt3532216'),
        Movie("Assassin's Creed", 'Action', 5.6, False, ['Hulu'], 'tt2094766'),
        Movie('Behind Enemy Lines', 'Action', 6.4, False, ['Paramount+'], 'tt0159273'),
        Movie('Blacklight', 'Action', 4.8, False, ['Hulu'], 'tt14060094'),
        Movie('Cliffhanger', 'Action', 6.5, False, ['Netflix'], 'tt0106582'),
        Movie('Die Hard', 'Action', 8.2, False, [], 'tt0095016'),
        Movie('Enemy at the Gates', 'Action', 7.5, False, ['Paramount+'], 'tt0215750'),
        Movie('Fast & Furious', 'Action', 6.5, False, ['Peacock'], 'tt1013752'),
        Movie('Fast Five', 'Action', 7.3, False, ['Peacock'], 'tt1596343'),
        Movie('First Blood', 'Action', 7.7, False, ['Paramount+'], 'tt0083944'),
        Movie('Four Brothers', 'Action', 6.8, False, ['Paramount+'], 'tt0430105'),
        Movie('Fury', 'Action', 7.6, False, ['Netflix'], 'tt2713180'),
        Movie('Gladiator', 'Action', 8.5, False, [], 'tt0172495'),
        Movie('Inception', 'Action', 8.8, False, [], 'tt1375666'),
        Movie('John Wick', 'Action', 7.5, False, [], 'tt2911666'),
        Movie('Jumanji: Welcome to the Jungle', 'Action', 6.9, False, ['Hulu'], 'tt2283362'),
        Movie('Jurassic World: Fallen Kingdom', 'Action', 6.1, False, ['Max (HBO Max)'], 'tt4881806'),
        Movie('Knight and Day', 'Action', 6.3, False, ['Hulu'], 'tt1013743'),
        Movie('Lone Survivor', 'Action', 7.5, False, ['Peacock'], 'tt1091191'),
        Movie('Mad Max: Fury Road', 'Action', 8.1, False, [], 'tt1392190'),
        Movie('Mission: Impossible - Fallout', 'Action', 7.7, False, [], 'tt4912910'),
        Movie('Sherlock Holmes: A Game of Shadows', 'Action', 7.4, False, ['Max (HBO Max)'], 'tt1515091'),
        Movie('Skyscraper', 'Action', 5.8, False, ['Max (HBO Max)'], 'tt5758778'),
        Movie('Spy Kids', 'Action', 5.6, False, ['Peacock'], 'tt0227538'),
        Movie('The Avengers', 'Action', 8.0, False, [], 'tt0848228'),
        Movie('The Chronicles of Narnia: The Voyage of the Dawn Treader', 'Action', 6.3, False, ['Hulu', 'Peacock'], 'tt0980970'),
        Movie('The Dark Knight', 'Action', 9.1, False, [], 'tt0468569'),
        Movie('The Fast and the Furious', 'Action', 6.8, False, ['Peacock'], 'tt0232500'),
        Movie('The Fast and the Furious: Tokyo Drift', 'Action', 6.1, False, ['Peacock'], 'tt0463985'),
        Movie("The Hitman's Bodyguard", 'Action', 6.9, False, ['Peacock'], 'tt1959563'),
        Movie("The Hitman's Wife's Bodyguard", 'Action', 6.1, False, ['Peacock'], 'tt8385148'),
        Movie('The Matrix', 'Action', 8.7, False, [], 'tt0133093'),
        Movie('The Mummy', 'Action', 7.1, False, ['Netflix'], 'tt0120616'),
        Movie('The Predator', 'Action', 5.3, False, ['Max (HBO Max)'], 'tt3829266'),
        Movie('The Wolverine', 'Action', 6.7, False, ['Max (HBO Max)'], 'tt1430132'),
        Movie('Top Gun: Maverick', 'Action', 8.2, False, [], 'tt1745960'),
        Movie('13 Going on 30', 'Comedy', 6.3, False, ['Paramount+'], 'tt0337563'),
        Movie('21 Jump Street', 'Comedy', 7.2, False, [], 'tt1232829'),
        Movie('A Bad Moms Christmas', 'Comedy', 5.6, False, ['Hulu', 'Peacock'], 'tt6359956'),
        Movie('A Christmas Story', 'Comedy', 7.9, False, ['Max (HBO Max)'], 'tt0085334'),
        Movie('A Very Harold & Kumar Christmas', 'Comedy', 6.2, False, ['Amazon Prime Video'], 'tt1268799'),
        Movie('Ace Ventura: Pet Detective', 'Comedy', 6.9, False, ['Hulu'], 'tt0109040'),
        Movie('Ace Ventura: When Nature Calls', 'Comedy', 6.4, False, ['Hulu'], 'tt0112281'),
        Movie('Almost Christmas', 'Comedy', 6.1, False, ['Hulu', 'Peacock'], 'tt4649416'),
        Movie('Annie Hall', 'Comedy', 8.0, False, ['Amazon Prime Video'], 'tt0075686'),
        Movie('Babe', 'Comedy', 6.9, False, ['Peacock'], 'tt0112431'),
        Movie('Bad Santa', 'Comedy', 7.0, False, ['Paramount+', 'Amazon Prime Video'], 'tt0307987'),
        Movie('Bad Santa 2', 'Comedy', 5.6, False, ['Paramount+', 'Amazon Prime Video'], 'tt1798603'),
        Movie('Beetlejuice', 'Comedy', 7.5, False, ['Peacock'], 'tt0094721'),
        Movie('Bridesmaids', 'Comedy', 6.8, False, ['Netflix'], 'tt1478338'),
        Movie('Cheaper by the Dozen', 'Comedy', 5.9, False, ['Hulu'], 'tt0349205'),
        Movie('Christmas with the Kranks', 'Comedy', 5.5, False, ['Max (HBO Max)'], 'tt0388419'),
        Movie('Despicable Me', 'Comedy', 7.6, False, ['Peacock'], 'tt1323594'),
        Movie('Dinner for Schmucks', 'Comedy', 5.9, False, ['Paramount+'], 'tt0427152'),
        Movie('Duck Soup', 'Comedy', 7.8, False, ['Amazon Prime Video'], 'tt0023969'),
        Movie('Dumb and Dumber', 'Comedy', 7.3, False, [], 'tt0109686'),
        Movie('Elf', 'Comedy', 7.1, False, ['Max (HBO Max)', 'Amazon Prime Video'], 'tt0319343'),
        Movie("Ferris Bueller's Day Off", 'Comedy', 7.8, False, [], 'tt0091042'),
        Movie('Get Shorty', 'Comedy', 6.9, False, ['Amazon Prime Video'], 'tt0113161'),
        Movie('Happy Feet', 'Comedy', 6.4, False, ['Max (HBO Max)', 'Paramount+'], 'tt0366548'),
        Movie('Hitch', 'Comedy', 6.6, False, ['Paramount+'], 'tt0386588'),
        Movie('Hook', 'Comedy', 6.8, False, ['Paramount+'], 'tt0102057'),
        Movie('Hot Tub Time Machine', 'Comedy', 6.4, False, ['Amazon Prime Video'], 'tt1231587'),
        Movie('Identity Thief', 'Comedy', 5.7, False, ['Peacock'], 'tt2024432'),
        Movie('Instant Family', 'Comedy', 7.3, False, ['Paramount+'], 'tt7401588'),
        Movie('Kung Fu Panda', 'Comedy', 7.6, False, ['Peacock'], 'tt0441773'),
        Movie('Last Holiday', 'Comedy', 6.6, False, ['Paramount+', 'Amazon Prime Video'], 'tt0408985'),
        Movie('Love Actually', 'Comedy', 7.6, False, ['Peacock'], 'tt0314331'),
        Movie('Love, Rosie', 'Comedy', 7.1, False, ['Paramount+'], 'tt1638002'),
        Movie('Madagascar', 'Comedy', 6.9, False, ['Peacock'], 'tt0351283'),
        Movie('Madagascar: Escape 2 Africa', 'Comedy', 6.6, False, ['Peacock'], 'tt0479952'),
        Movie('Mean Girls', 'Comedy', 7.1, False, ['Amazon Prime Video'], 'tt0377092'),
        Movie('Meet the Fockers', 'Comedy', 6.3, False, ['Peacock'], 'tt0290002'),
        Movie('Meet the Parents', 'Comedy', 7.0, False, ['Peacock'], 'tt0212338'),
        Movie("National Lampoon's Christmas Vacation", 'Comedy', 7.5, False, ['Max (HBO Max)'], 'tt0097958'),
        Movie('No Hard Feelings', 'Comedy', 6.4, False, ['Amazon Prime Video'], 'tt15671028'),
        Movie('No Strings Attached', 'Comedy', 6.2, False, ['Paramount+'], 'tt1411238'),
        Movie('Norbit', 'Comedy', 4.2, False, ['Paramount+'], 'tt0477051'),
        Movie('Notting Hill', 'Comedy', 7.2, False, ['Peacock'], 'tt0125439'),
        Movie('Office Space', 'Comedy', 7.6, False, [], 'tt0151804'),
        Movie('Planes, Trains and Automobiles', 'Comedy', 7.6, False, ['Peacock'], 'tt0093748'),
        Movie('Project X', 'Comedy', 6.7, False, ['Max (HBO Max)'], 'tt1636826'),
        Movie('Rango', 'Comedy', 7.3, False, ['Peacock'], 'tt1192628'),
        Movie('Rise of the Guardians', 'Comedy', 7.2, False, ['Max (HBO Max)', 'Peacock'], 'tt1446192'),
        Movie('Soul', 'Comedy', 8.0, False, ['Disney+'], 'tt2948372'),
        Movie('Spirited', 'Comedy', 6.6, False, ['Apple TV'], 'tt10999120'),
        Movie('Step Brothers', 'Comedy', 6.9, False, [], 'tt0838283'),
        Movie('Superbad', 'Comedy', 7.6, False, [], 'tt0829482'),
        Movie('Sweet Home Alabama', 'Comedy', 6.2, False, ['Peacock'], 'tt0256415'),
        Movie('The Big Lebowski', 'Comedy', 8.1, False, [], 'tt0118715'),
        Movie('The Croods', 'Comedy', 7.1, False, ['Netflix', 'Peacock'], 'tt0481499'),
        Movie('The Devil Wears Prada', 'Comedy', 7.0, False, ['Hulu'], 'tt0458352'),
        Movie('The Family Stone', 'Comedy', 6.3, False, ['Hulu'], 'tt0356680'),
        Movie('The Grand Budapest Hotel', 'Comedy', 8.1, False, [], 'tt2278388'),
        Movie('The Hangover', 'Comedy', 7.7, False, [], 'tt1119646'),
        Movie('The Polar Express', 'Comedy', 6.6, False, ['Max (HBO Max)'], 'tt0338348'),
        Movie('The Princess Bride', 'Comedy', 8.0, False, ['Peacock'], 'tt0093779'),
        Movie('The Secret Life of Pets', 'Comedy', 6.5, False, ['Peacock'], 'tt2709768'),
        Movie('The Secret Life of Pets 2', 'Comedy', 6.4, False, ['Peacock'], 'tt5113040'),
        Movie('The Secret Life of Walter Mitty', 'Comedy', 7.3, False, ['Hulu'], 'tt0359950'),
        Movie('Trolls', 'Comedy', 6.4, False, ['Peacock'], 'tt1679335'),
        Movie('Turning Red', 'Comedy', 6.9, False, ['Disney+'], 'tt8097030'),
        Movie("Weekend at Bernie's", 'Comedy', 6.4, False, ['Netflix'], 'tt0098627'),
        Movie('Why Him?', 'Comedy', 6.2, False, ['Hulu'], 'tt4501244'),
        Movie('Wild Hogs', 'Comedy', 5.8, False, ['Hulu'], 'tt0486946'),
        Movie('A Beautiful Day in the Neighborhood', 'Drama', 7.2, False, ['Peacock'], 'tt3224458'),
        Movie('American Sniper', 'Drama', 7.3, False, ['Peacock'], 'tt2179136'),
        Movie('An Officer and a Gentleman', 'Drama', 7.1, False, ['Paramount+'], 'tt0084434'),
        Movie('Beautiful Girls', 'Drama', 7.1, False, ['Paramount+'], 'tt0115639'),
        Movie('Belfast', 'Drama', 7.2, False, ['Peacock'], 'tt12789558'),
        Movie("Breakfast at Tiffany's", 'Drama', 7.6, False, ['Paramount+'], 'tt0054698'),
        Movie('Coach Carter', 'Drama', 7.3, False, ['Paramount+'], 'tt0393162'),
        Movie('CODA', 'Drama', 8.0, False, ['Apple TV'], 'tt10366460'),
        Movie('Cold Mountain', 'Drama', 7.2, False, ['Paramount+'], 'tt0159365'),
        Movie('Darkest Hour', 'Drama', 7.4, False, ['Amazon Prime Video'], 'tt4555426'),
        Movie('Dead Poets Society', 'Drama', 8.1, False, [], 'tt0097165'),
        Movie('Doubt', 'Drama', 7.5, False, ['Paramount+'], 'tt0918927'),
        Movie('Dreamgirls', 'Drama', 6.6, False, ['Paramount+'], 'tt0443489'),
        Movie('Fight Club', 'Drama', 8.8, False, [], 'tt0137523'),
        Movie('Flags of Our Fathers', 'Drama', 7.1, False, ['Paramount+'], 'tt0418689'),
        Movie('Footloose', 'Drama', 6.6, False, ['Paramount+'], 'tt0087277'),
        Movie('Forrest Gump', 'Drama', 8.8, False, [], 'tt0109830'),
        Movie('Gifted', 'Drama', 7.6, False, ['Peacock'], 'tt4481414'),
        Movie('Good Will Hunting', 'Drama', 8.3, False, ['Amazon Prime Video'], 'tt0119217'),
        Movie('Hacksaw Ridge', 'Drama', 8.1, False, ['Peacock'], 'tt2119532'),
        Movie('Hugo', 'Drama', 7.5, False, ['Paramount+'], 'tt0970179'),
        Movie('In the Heat of the Night', 'Drama', 7.9, False, ['Amazon Prime Video'], 'tt0061811'),
        Movie("It's a Wonderful Life", 'Drama', 8.6, False, ['Paramount+', 'Peacock'], 'tt0038650'),
        Movie('Jerry Maguire', 'Drama', 7.3, False, ['Max (HBO Max)'], 'tt0116695'),
        Movie('Killers of the Flower Moon', 'Drama', 7.5, False, ['Apple TV'], 'tt5537002'),
        Movie('Manchester by the Sea', 'Drama', 7.8, False, [], 'tt4034228'),
        Movie('Miracle', 'Drama', 7.4, False, ['Hulu'], 'tt0349825'),
        Movie('Pride and Prejudice', 'Drama', 7.8, False, ['Peacock'], 'tt0414387'),
        Movie('Public Enemies', 'Drama', 7.0, False, ['Netflix'], 'tt1152836'),
        Movie('Richard Jewell', 'Drama', 7.5, False, ['Netflix'], 'tt3513548'),
        Movie('Scent of a Woman', 'Drama', 8.0, False, ['Peacock'], 'tt0105323'),
        Movie('Stand by Me', 'Drama', 8.1, False, ['Netflix'], 'tt0092005'),
        Movie('The Banshees of Inisherin', 'Drama', 7.7, False, ['Hulu'], 'tt11813216'),
        Movie('The Godfather', 'Drama', 9.2, False, [], 'tt0068646'),
        Movie('The Last Duel', 'Drama', 7.3, False, ['Hulu'], 'tt4244994'),
        Movie('The Pursuit of Happyness', 'Drama', 8.0, False, [], 'tt0454921'),
        Movie('The Shawshank Redemption', 'Drama', 9.3, False, [], 'tt0111161'),
        Movie('The Social Network', 'Drama', 7.8, False, [], 'tt1285016'),
        Movie('Unbroken', 'Drama', 7.2, False, ['Peacock'], 'tt1809398'),
        Movie('Up in the Air', 'Drama', 7.4, False, ['Peacock'], 'tt1193138'),
        Movie('Whiplash', 'Drama', 8.5, False, ['Netflix'], 'tt2582802'),
        Movie('A Quiet Place', 'Horror', 7.5, False, [], 'tt6644200'),
        Movie("Don't Breathe", 'Horror', 7.1, False, ['Hulu'], 'tt4160708'),
        Movie('Get Out', 'Horror', 7.8, False, [], 'tt5052448'),
        Movie('Gretel & Hansel', 'Horror', 5.5, False, ['Amazon Prime Video'], 'tt9086228'),
        Movie('Halloween', 'Horror', 7.7, False, [], 'tt0077651'),
        Movie('Heart Eyes', 'Horror', 6.1, False, ['Hulu'], 'tt32558992'),
        Movie('Hereditary', 'Horror', 7.3, False, [], 'tt7784604'),
        Movie('Insidious: Chapter 2', 'Horror', 6.6, False, ['Netflix'], 'tt2226417'),
        Movie('Insidious: Chapter 3', 'Horror', 6.1, False, ['Netflix'], 'tt3195644'),
        Movie('It', 'Horror', 7.3, False, [], 'tt1396484'),
        Movie('Jeepers Creepers', 'Horror', 6.2, False, ['Amazon Prime Video'], 'tt0263488'),
        Movie('Jeepers Creepers 2', 'Horror', 5.6, False, ['Amazon Prime Video'], 'tt0301470'),
        Movie('Resident Evil', 'Horror', 6.6, False, ['Netflix'], 'tt0120804'),
        Movie('Resident Evil: Apocalypse', 'Horror', 6.1, False, ['Netflix'], 'tt0318627'),
        Movie('Scream', 'Horror', 7.4, False, ['Max (HBO Max)'], 'tt0117571'),
        Movie('The Babadook', 'Horror', 6.8, False, [], 'tt2321549'),
        Movie('The Conjuring', 'Horror', 7.5, False, [], 'tt1457767'),
        Movie('The Exorcist', 'Horror', 8.1, False, [], 'tt0070047'),
        Movie('The First Purge', 'Horror', 5.2, False, ['Max (HBO Max)'], 'tt6133466'),
        Movie('The Shining', 'Horror', 8.4, False, [], 'tt0081505'),
        Movie('The Texas Chain Saw Massacre', 'Horror', 7.4, False, [], 'tt0072271'),
        Movie('2001: A Space Odyssey', 'Sci-Fi', 8.3, False, [], 'tt0062622'),
        Movie('2012', 'Sci-Fi', 5.8, False, ['Peacock'], 'tt1190080'),
        Movie('Aliens', 'Sci-Fi', 8.4, False, ['Hulu'], 'tt0090605'),
        Movie('Arrival', 'Sci-Fi', 7.9, False, [], 'tt2543164'),
        Movie('Back to the Future', 'Sci-Fi', 8.5, False, [], 'tt0088763'),
        Movie('Blade Runner 2049', 'Sci-Fi', 8.0, False, [], 'tt1856101'),
        Movie('Dawn of the Planet of the Apes', 'Sci-Fi', 7.6, False, ['Max (HBO Max)'], 'tt2103281'),
        Movie('District 9', 'Sci-Fi', 7.9, False, [], 'tt1136608'),
        Movie('Dune', 'Sci-Fi', 6.3, False, ['Max (HBO Max)'], 'tt0087182'),
        Movie('Dune: Part Two', 'Sci-Fi', 8.5, False, [], 'tt15239678'),
        Movie('Edge of Tomorrow', 'Sci-Fi', 7.9, False, [], 'tt1631867'),
        Movie('Ex Machina', 'Sci-Fi', 7.7, False, [], 'tt0470752'),
        Movie('Interstellar', 'Sci-Fi', 8.7, False, ['Paramount+'], 'tt0816692'),
        Movie('Kingdom of the Planet of the Apes', 'Sci-Fi', 6.8, False, ['Max (HBO Max)'], 'tt11389872'),
        Movie('Looper', 'Sci-Fi', 7.4, False, ['Netflix'], 'tt1276104'),
        Movie('Meg 2: The Trench', 'Sci-Fi', 5.0, False, ['Hulu'], 'tt9224104'),
        Movie('Rise of the Planet of the Apes', 'Sci-Fi', 7.6, False, ['Max (HBO Max)'], 'tt1318514'),
        Movie('The Day After Tomorrow', 'Sci-Fi', 6.5, False, ['Netflix'], 'tt0319262'),
        Movie('The Martian', 'Sci-Fi', 8.0, False, [], 'tt3659388'),
        Movie('The Meg', 'Sci-Fi', 5.7, False, ['Hulu'], 'tt4779682'),
        Movie('War for the Planet of the Apes', 'Sci-Fi', 7.4, False, ['Hulu', 'Max (HBO Max)'], 'tt3450958'),
        Movie('Allied', 'Thriller', 7.1, False, ['Paramount+'], 'tt3640424'),
        Movie('Black Bag', 'Thriller', 6.7, False, ['Hulu'], 'tt30988739'),
        Movie('Blink Twice', 'Thriller', 6.5, False, ['Amazon Prime Video'], 'tt14858658'),
        Movie('End of Watch', 'Thriller', 7.6, False, ['Peacock'], 'tt1855199'),
        Movie('Enemy', 'Thriller', 6.9, False, ['Max (HBO Max)'], 'tt2316411'),
        Movie('Fargo', 'Thriller', 8.1, False, ['Peacock'], 'tt0116282'),
        Movie('Gone Girl', 'Thriller', 8.1, False, ['Paramount+'], 'tt2267998'),
        Movie('Hard Eight', 'Thriller', 7.1, False, ['Paramount+'], 'tt0119256'),
        Movie('Memento', 'Thriller', 8.4, False, [], 'tt0209144'),
        Movie('Nightcrawler', 'Thriller', 7.8, False, ['Peacock'], 'tt2872718'),
        Movie('No Country for Old Men', 'Thriller', 8.2, False, [], 'tt0477348'),
        Movie('Now You See Me', 'Thriller', 7.2, False, ['Peacock'], 'tt1670345'),
        Movie('Now You See Me 2', 'Thriller', 6.4, False, ['Peacock'], 'tt3110958'),
        Movie('Prisoners', 'Thriller', 8.2, False, [], 'tt1392214'),
        Movie('Red Sparrow', 'Thriller', 6.6, False, ['Max (HBO Max)'], 'tt2873282'),
        Movie('Se7en', 'Thriller', 8.6, False, [], 'tt0114369'),
        Movie('Shutter Island', 'Thriller', 8.2, False, [], 'tt1130884'),
        Movie('The Prestige', 'Thriller', 8.5, False, [], 'tt0482571'),
        Movie('The Silence of the Lambs', 'Thriller', 8.6, False, [], 'tt0102926'),
        Movie('Unhinged', 'Thriller', 6.0, False, ['Hulu'], 'tt10059518'),
        Movie('Zodiac', 'Thriller', 7.7, False, [], 'tt0443706'),
    ]

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

    Div(
        RelatedCheckBox("services", "Netflix", "Netflix" in state.selected_services),
        " Netflix",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "Hulu", "Hulu" in state.selected_services),
        " Hulu",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "Disney+", "Disney+" in state.selected_services),
        " Disney+",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "Max (HBO Max)", "Max (HBO Max)" in state.selected_services),
        " Max (HBO Max)",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "Amazon Prime Video", "Amazon Prime Video" in state.selected_services),
        " Amazon Prime Video",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "Paramount+", "Paramount+" in state.selected_services),
        " Paramount+",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "Peacock", "Peacock" in state.selected_services),
        " Peacock",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "Apple TV", "Apple TV" in state.selected_services),
        " Apple TV",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "Tubi (Free)", "Tubi (Free)" in state.selected_services),
        " Tubi (Free)",
        style_margin="8px 0"
    ),
    Div(
        RelatedCheckBox("services", "AMC+", "AMC+" in state.selected_services),
        " AMC+",
        style_margin="8px 0"
    )
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
