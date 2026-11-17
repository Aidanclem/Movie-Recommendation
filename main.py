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
        Movie('The Thing', 'Horror', 8.2, False, ['Amazon Prime Video'], 'tt0084787'),
        Movie('Alien', 'Sci-Fi', 8.4, False, ['Netflix'], 'tt0078748'),
        Movie('Pulp Fiction', 'Thriller', 8.8, False, ['Paramount+', 'Apple TV'], 'tt0110912'),
        Movie('The Fly', 'Horror', 7.6, False, [], 'tt0091064'),
        Movie('Alien 3', 'Sci-Fi', 6.4, False, [], 'tt0103644'),
        Movie('Reservoir Dogs', 'Thriller', 8.2, False, ['Amazon Prime Video'], 'tt0105236'),
        Movie('The Blob', 'Horror', 6.7, False, [], 'tt0094761'),
        Movie('Alien Resurrection', 'Sci-Fi', 6.2, False, [], 'tt0118583'),
        Movie('Jackie Brown', 'Thriller', 7.5, False, [], 'tt0119396'),
        Movie('The Mist', 'Horror', 7.1, False, ['Amazon Prime Video'], 'tt0884328'),
        Movie('Prometheus', 'Sci-Fi', 7.0, False, [], 'tt1446714'),
        Movie('Death Proof', 'Thriller', 7.0, False, [], 'tt1028528'),
        Movie('The Fog', 'Horror', 6.8, False, [], 'tt0080749'),
        Movie('Alien: Covenant', 'Sci-Fi', 6.4, False, [], 'tt2316204'),
        Movie('True Romance', 'Thriller', 7.9, False, [], 'tt0108399'),
        Movie('The Descent', 'Horror', 7.2, False, [], 'tt0435625'),
        Movie('Alien: Romulus', 'Sci-Fi', 7.1, False, ['Hulu'], 'tt18412256'),
        Movie('Natural Born Killers', 'Thriller', 7.2, False, [], 'tt0110632'),
        Movie('The Descent Part 2', 'Horror', 5.7, False, [], 'tt1073105'),
        Movie('Blade Runner', 'Sci-Fi', 8.1, False, [], 'tt0083658'),
        Movie('The Usual Suspects', 'Thriller', 8.5, False, [], 'tt0114814'),
        Movie('The Ritual', 'Horror', 6.4, False, ['Netflix'], 'tt5638642'),
        Movie('The Matrix Reloaded', 'Sci-Fi', 7.2, False, [], 'tt0234215'),
        Movie('L.A. Confidential', 'Thriller', 8.2, False, [], 'tt0119488'),
        Movie('The Witch', 'Horror', 7.0, False, ['Amazon Prime Video'], 'tt4263482'),
        Movie('The Matrix Revolutions', 'Sci-Fi', 6.8, False, [], 'tt0242653'),
        Movie('The Negotiator', 'Thriller', 7.3, False, [], 'tt0120768'),
        Movie('The Lighthouse', 'Horror', 7.3, False, ['Max (HBO Max)'], 'tt7984734'),
        Movie('The Matrix Resurrections', 'Sci-Fi', 5.6, False, [], 'tt10838180'),
        Movie('The Game', 'Thriller', 7.7, False, [], 'tt0119174'),
        Movie('Midsommar', 'Horror', 7.1, False, [], 'tt8772262'),
        Movie('The Animatrix', 'Sci-Fi', 7.3, False, [], 'tt0328832'),
        Movie('Panic Room', 'Thriller', 6.9, False, [], 'tt0258000'),
        Movie('The Wicker Man', 'Horror', 7.5, False, [], 'tt0070917'),
        Movie('The Fifth Element', 'Sci-Fi', 7.6, False, [], 'tt0119116'),
        Movie('The Girl with the Dragon Tattoo', 'Thriller', 7.8, False, ['Netflix'], 'tt1568346'),
        Movie('The Blair Witch Project', 'Horror', 6.5, False, [], 'tt0185937'),
        Movie('Total Recall', 'Sci-Fi', 7.5, False, [], 'tt0100802'),
        Movie('The Girl on the Train', 'Thriller', 6.5, False, [], 'tt3631112'),
        Movie('Blair Witch', 'Horror', 5.0, False, [], 'tt1540011'),
        Movie('Total Recall (2012)', 'Sci-Fi', 6.2, False, [], 'tt1386703'),
        Movie('The Woman in the Window', 'Thriller', 5.7, False, [], 'tt6111574'),
        Movie('Paranormal Activity', 'Horror', 6.3, False, ['Paramount+'], 'tt1179904'),
        Movie('Minority Report', 'Sci-Fi', 7.6, False, [], 'tt0181689'),
        Movie('The Woman in Cabin 10', 'Thriller', 5.8, False, ['Netflix'], 'tt7130300'),
        Movie('Paranormal Activity 2', 'Horror', 5.7, False, [], 'tt1536044'),
        Movie('War of the Worlds', 'Sci-Fi', 6.6, False, [], 'tt0407304'),
        Movie('The Invisible Guest', 'Thriller', 8.0, False, [], 'tt4857264'),
        Movie('Paranormal Activity 3', 'Horror', 5.8, False, [], 'tt1778304'),
        Movie('War of the Worlds (1953)', 'Sci-Fi', 7.0, False, [], 'tt0046534'),
        Movie('The Body', 'Thriller', 7.6, False, [], 'tt1937149'),
        Movie('Paranormal Activity 4', 'Horror', 4.7, False, [], 'tt2109184'),
        Movie('The Secret in Their Eyes', 'Thriller', 8.2, False, [], 'tt1305806'),
        Movie('Paranormal Activity: The Marked Ones', 'Horror', 5.1, False, [], 'tt2473682'),
        Movie('Independence Day', 'Sci-Fi', 7.0, False, [], 'tt0116629'),
        Movie('The Lives of Others', 'Thriller', 8.4, False, [], 'tt0405094'),
        Movie('Paranormal Activity: The Ghost Dimension', 'Horror', 4.6, False, [], 'tt2473510'),
        Movie('Independence Day: Resurgence', 'Sci-Fi', 5.2, False, [], 'tt1628841'),
        Movie('The Conversation', 'Thriller', 7.7, False, [], 'tt0071360'),
        Movie('The Godfather Part II', 'Drama', 9.0, False, [], 'tt0071562'),
        Movie('Sinister', 'Horror', 6.8, False, [], 'tt1922777'),
        Movie('Men in Black', 'Sci-Fi', 7.3, False, [], 'tt0119654'),
        Movie('Blow Out', 'Thriller', 7.4, False, [], 'tt0082085'),
        Movie('The Dark Knight Rises', 'Action', 8.4, False, ['Max (HBO Max)'], 'tt1345836'),
        Movie('The Godfather Part III', 'Drama', 7.5, False, [], 'tt0099674'),
        Movie('Sinister 2', 'Horror', 5.3, False, [], 'tt2752772'),
        Movie('Men in Black II', 'Sci-Fi', 6.2, False, [], 'tt0120912'),
        Movie('Blow-Up', 'Thriller', 7.4, False, [], 'tt0060176'),
        Movie('Batman Begins', 'Action', 8.2, False, [], 'tt0372784'),
        Movie('The Irishman', 'Drama', 7.8, False, ['Netflix'], 'tt1302006'),
        Movie('Insidious', 'Horror', 6.8, False, [], 'tt1591095'),
        Movie('Men in Black 3', 'Sci-Fi', 6.8, False, [], 'tt1409024'),
        Movie('Rear Window', 'Thriller', 8.4, False, [], 'tt0047396'),
        Movie('The Batman', 'Action', 7.8, False, [], 'tt1877830'),
        Movie('Goodfellas', 'Drama', 8.7, False, [], 'tt0099685'),
        Movie('Insidious: The Last Key', 'Horror', 5.7, False, [], 'tt5726086'),
        Movie('Men in Black: International', 'Sci-Fi', 5.6, False, [], 'tt2283336'),
        Movie('Vertigo', 'Thriller', 8.2, False, [], 'tt0052357'),
        Movie('Batman', 'Action', 7.5, False, [], 'tt0096895'),
        Movie('Casino', 'Drama', 8.2, False, [], 'tt0112641'),
        Movie('Insidious: The Red Door', 'Horror', 5.5, False, [], 'tt13405778'),
        Movie('Star Wars', 'Sci-Fi', 8.6, False, ['Disney+'], 'tt0076759'),
        Movie('Psycho', 'Thriller', 8.5, False, [], 'tt0054215'),
        Movie('Batman Returns', 'Action', 7.1, False, [], 'tt0103776'),
        Movie('A Bronx Tale', 'Drama', 7.8, False, [], 'tt0106489'),
        Movie('The Conjuring 2', 'Horror', 7.3, False, [], 'tt3065204'),
        Movie('The Empire Strikes Back', 'Sci-Fi', 8.7, False, [], 'tt0080684'),
        Movie('North by Northwest', 'Thriller', 8.2, False, [], 'tt0053125'),
        Movie('Batman Forever', 'Action', 5.5, False, [], 'tt0112462'),
        Movie('Once Upon a Time in America', 'Drama', 8.3, False, [], 'tt0087843'),
        Movie('The Conjuring: The Devil Made Me Do It', 'Horror', 6.2, False, [], 'tt7069210'),
        Movie('Return of the Jedi', 'Sci-Fi', 8.3, False, [], 'tt0086190'),
        Movie('Strangers on a Train', 'Thriller', 7.9, False, [], 'tt0044079'),
        Movie('Batman & Robin', 'Action', 3.8, False, [], 'tt0118688'),
        Movie('The Departed', 'Drama', 8.5, False, [], 'tt0407887'),
        Movie('Annabelle', 'Horror', 5.5, False, [], 'tt3322940'),
        Movie('The Phantom Menace', 'Sci-Fi', 6.5, False, ['Disney+'], 'tt0120915'),
        Movie('Dial M for Murder', 'Thriller', 8.1, False, [], 'tt0046912'),
        Movie('Superman', 'Action', 7.4, False, [], 'tt0078346'),
        Movie('The Aviator', 'Drama', 7.5, False, [], 'tt0338751'),
        Movie('Annabelle: Creation', 'Horror', 6.5, False, [], 'tt5140878'),
        Movie('Attack of the Clones', 'Sci-Fi', 6.6, False, [], 'tt0121765'),
        Movie('Rope', 'Thriller', 7.9, False, [], 'tt0040746'),
        Movie('Superman II', 'Action', 6.8, False, [], 'tt0081573'),
        Movie('The Wolf of Wall Street', 'Drama', 8.2, False, [], 'tt0993846'),
        Movie('Annabelle Comes Home', 'Horror', 5.9, False, [], 'tt8350360'),
        Movie('Revenge of the Sith', 'Sci-Fi', 7.7, False, [], 'tt0121766'),
        Movie('Rebecca', 'Thriller', 8.0, False, [], 'tt0032976'),
        Movie('Superman Returns', 'Action', 6.1, False, [], 'tt0348150'),
        Movie('Raging Bull', 'Drama', 8.1, False, [], 'tt0081398'),
        Movie('The Nun', 'Horror', 5.4, False, [], 'tt5814060'),
        Movie('The Force Awakens', 'Sci-Fi', 7.7, False, ['Disney+'], 'tt2488496'),
        Movie('Notorious', 'Thriller', 7.9, False, [], 'tt0038787'),
        Movie('Man of Steel', 'Action', 7.1, False, [], 'tt0770828'),
        Movie('Taxi Driver', 'Drama', 8.2, False, [], 'tt0075314'),
        Movie('The Nun II', 'Horror', 5.6, False, [], 'tt10160976'),
        Movie('The Last Jedi', 'Sci-Fi', 6.8, False, ['Disney+'], 'tt2527336'),
        Movie('Shadow of a Doubt', 'Thriller', 7.7, False, [], 'tt0036342'),
        Movie('Batman v Superman: Dawn of Justice', 'Action', 6.4, False, [], 'tt2975590'),
        Movie('Mean Streets', 'Drama', 7.1, False, [], 'tt0070379'),
        Movie('The Curse of La Llorona', 'Horror', 5.3, False, [], 'tt4913966'),
        Movie('The Rise of Skywalker', 'Sci-Fi', 6.3, False, ['Disney+'], 'tt2527338'),
        Movie('The Birds', 'Thriller', 7.6, False, [], 'tt0056869'),
        Movie("Zack Snyder's Justice League", 'Action', 7.9, False, [], 'tt12361974'),
        Movie('The King of Comedy', 'Drama', 7.8, False, [], 'tt0085794'),
        Movie('The Exorcist III', 'Horror', 6.5, False, [], 'tt0099528'),
        Movie('Rogue One: A Star Wars Story', 'Sci-Fi', 7.8, False, ['Disney+'], 'tt3748528'),
        Movie('Frenzy', 'Thriller', 7.4, False, [], 'tt0068611'),
        Movie('Justice League', 'Action', 6.0, False, [], 'tt0974015'),
        Movie('The Age of Innocence', 'Drama', 7.2, False, [], 'tt0106226'),
        Movie('Exorcist II: The Heretic', 'Horror', 3.8, False, [], 'tt0076009'),
        Movie('Solo: A Star Wars Story', 'Sci-Fi', 6.9, False, ['Disney+'], 'tt3778644'),
        Movie('The 39 Steps', 'Thriller', 7.6, False, [], 'tt0026029'),
        Movie('Wonder Woman', 'Action', 7.3, False, [], 'tt0451279'),
        Movie('Silence', 'Drama', 7.2, False, [], 'tt0490215'),
        Movie('The Exorcist: Believer', 'Horror', 4.8, False, [], 'tt12921446'),
        Movie('Star Trek: The Motion Picture', 'Sci-Fi', 6.4, False, ['Paramount+'], 'tt0079945'),
        Movie('The Man Who Knew Too Much', 'Thriller', 7.4, False, [], 'tt0049470'),
        Movie('Wonder Woman 1984', 'Action', 5.3, False, [], 'tt7126948'),
        Movie('The Last Temptation of Christ', 'Drama', 7.5, False, [], 'tt0095497'),
        Movie('The Last Exorcism', 'Horror', 5.7, False, [], 'tt1320244'),
        Movie('Star Trek II: The Wrath of Khan', 'Sci-Fi', 7.7, False, ['Paramount+'], 'tt0084726'),
        Movie('The Lady Vanishes', 'Thriller', 7.7, False, [], 'tt0030341'),
        Movie('Aquaman', 'Action', 6.8, False, [], 'tt1477834'),
        Movie('Gangs of New York', 'Drama', 7.5, False, [], 'tt0217505'),
        Movie('The Exorcism of Emily Rose', 'Horror', 6.7, False, [], 'tt0404032'),
        Movie('Star Trek III: The Search for Spock', 'Sci-Fi', 6.7, False, ['Paramount+'], 'tt0088170'),
        Movie('The Wrong Man', 'Thriller', 7.4, False, [], 'tt0051207'),
        Movie('Aquaman and the Lost Kingdom', 'Action', 5.6, False, [], 'tt9663764'),
        Movie('The Color of Money', 'Drama', 7.0, False, [], 'tt0090863'),
        Movie('The Omen', 'Horror', 7.5, False, [], 'tt0075005'),
        Movie('Star Trek IV: The Voyage Home', 'Sci-Fi', 7.3, False, ['Paramount+'], 'tt0092007'),
        Movie('The Lodger', 'Thriller', 7.3, False, [], 'tt0017075'),
        Movie('Shazam!', 'Action', 7.0, False, [], 'tt0448115'),
        Movie('The Last Waltz', 'Drama', 8.1, False, [], 'tt0077838'),
        Movie('Damien: Omen II', 'Horror', 6.2, False, [], 'tt0077394'),
        Movie('Star Trek V: The Final Frontier', 'Sci-Fi', 5.5, False, ['Paramount+'], 'tt0098382'),
        Movie('The Talented Mr. Ripley', 'Thriller', 7.4, False, [], 'tt0134119'),
        Movie('Black Adam', 'Action', 6.1, False, [], 'tt6443346'),
        Movie('The Insider', 'Drama', 7.8, False, [], 'tt0140352'),
        Movie('The Final Conflict', 'Horror', 5.5, False, [], 'tt0082377'),
        Movie('Star Trek VI: The Undiscovered Country', 'Sci-Fi', 7.3, False, ['Paramount+'], 'tt0102975'),
        Movie("Ripley's Game", 'Thriller', 6.6, False, [], 'tt0265651'),
        Movie('The Flash', 'Action', 6.6, False, [], 'tt0439572'),
        Movie('Heat', 'Drama', 8.3, False, [], 'tt0113277'),
        Movie('The First Omen', 'Horror', 6.5, False, [], 'tt5672290'),
        Movie('Star Trek: Generations', 'Sci-Fi', 6.6, False, ['Paramount+'], 'tt0111280'),
        Movie('A Simple Favor', 'Thriller', 6.7, False, [], 'tt7040874'),
        Movie('Blue Beetle', 'Action', 5.9, False, [], 'tt9362930'),
        Movie('Collateral', 'Drama', 7.5, False, [], 'tt0369339'),
        Movie("Rosemary's Baby", 'Horror', 8.0, False, [], 'tt0063522'),
        Movie('Star Trek: First Contact', 'Sci-Fi', 7.6, False, ['Paramount+'], 'tt0117731'),
        Movie('A Simple Plan', 'Thriller', 7.5, False, [], 'tt0120324'),
        Movie('Iron Man', 'Action', 7.9, False, ['Disney+', 'Hulu'], 'tt0371746'),
        Movie('The Last of the Mohicans', 'Drama', 7.6, False, [], 'tt0104691'),
        Movie('The Amityville Horror', 'Horror', 6.2, False, [], 'tt0078767'),
        Movie('Star Trek: Insurrection', 'Sci-Fi', 6.4, False, ['Paramount+'], 'tt0120844'),
        Movie('The Gift', 'Thriller', 6.7, False, [], 'tt0219699'),
        Movie('Iron Man 2', 'Action', 6.9, False, ['Disney+'], 'tt1228705'),
        Movie('Thief', 'Drama', 7.4, False, [], 'tt0083190'),
        Movie('The Amityville Horror (2005)', 'Horror', 5.9, False, [], 'tt0384806'),
        Movie('Star Trek: Nemesis', 'Sci-Fi', 6.4, False, ['Paramount+'], 'tt0253754'),
        Movie('The Gift (2015)', 'Thriller', 7.0, False, [], 'tt4178092'),
        Movie('Iron Man 3', 'Action', 7.1, False, ['Disney+'], 'tt1300854'),
        Movie('Miami Vice', 'Drama', 6.1, False, [], 'tt0430357'),
        Movie('Poltergeist', 'Horror', 7.3, False, [], 'tt0084516'),
        Movie('Star Trek', 'Sci-Fi', 7.9, False, ['Paramount+', 'Peacock'], 'tt0796366'),
        Movie('The Invitation', 'Thriller', 6.6, False, [], 'tt2400463'),
        Movie('The Incredible Hulk', 'Action', 6.6, False, ['Disney+'], 'tt0800080'),
        Movie('The Public Enemy', 'Drama', 7.5, False, [], 'tt0022286'),
        Movie('Poltergeist II: The Other Side', 'Horror', 5.7, False, [], 'tt0091778'),
        Movie('Star Trek Into Darkness', 'Sci-Fi', 7.7, False, ['Paramount+', 'Peacock'], 'tt1408101'),
        Movie('The Invitation (2015)', 'Thriller', 6.6, False, [], 'tt2400463'),
        Movie('Thor', 'Action', 7.0, False, ['Disney+'], 'tt0800369'),
        Movie('Scarface', 'Drama', 8.3, False, [], 'tt0086250'),
        Movie('Poltergeist III', 'Horror', 4.7, False, [], 'tt0095889'),
        Movie('Star Trek Beyond', 'Sci-Fi', 7.0, False, ['Paramount+', 'Peacock'], 'tt2660888'),
        Movie('The Invitation (2022)', 'Thriller', 5.3, False, [], 'tt12873562'),
        Movie('Thor: The Dark World', 'Action', 6.7, False, ['Disney+'], 'tt1981115'),
        Movie('Anchorman: The Legend of Ron Burgundy', 'Comedy', 7.1, False, [], 'tt0357413'),
        Movie("Carlito's Way", 'Drama', 7.9, False, [], 'tt0106519'),
        Movie('The Ring', 'Horror', 7.1, False, [], 'tt0298130'),
        Movie('Dune (2021)', 'Sci-Fi', 8.0, False, [], 'tt1160419'),
        Movie('Calibre', 'Thriller', 6.8, False, ['Netflix'], 'tt6218358'),
        Movie('Thor: Ragnarok', 'Action', 7.9, False, [], 'tt3501632'),
        Movie('Anchorman 2: The Legend Continues', 'Comedy', 6.3, False, [], 'tt1229340'),
        Movie('Donnie Brasco', 'Drama', 7.7, False, [], 'tt0119008'),
        Movie('The Ring Two', 'Horror', 5.4, False, [], 'tt0377109'),
        Movie('Children of Men', 'Sci-Fi', 7.9, False, [], 'tt0206634'),
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
