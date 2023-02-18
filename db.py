def get_games():
    games = [
        {
            "id": "fca92ad7-8468-4c84-97ef-397e03e6c56e",
            "name": "star-realms",
            "timeCreated": 1659776105,
            "displayName": "Star Realms",
            "synopsis": "Compete head-to-head to create the most powerful deck of spaceships and bases.",
            "description": "Star Realms is a spaceship combat deck-building game by Magic Hall of Famers Darwin Kastle (The Battle for Hill 218) and Rob Dougherty (Ascension Co-designer).\n\nStar Realms is a fast paced deck-building card game of outer space combat. It combines the fun of a deck-building game with the interactivity of Trading Card Game style combat. As you play, you make use of Trade to acquire new Ships and Bases from the cards being turned face up in the Trade Row from the Trade Deck. You use the Ships and Bases you acquire to either generate more Trade or to generate Combat to attack your opponent and their bases. When you reduce your opponent’s score (called Authority) to zero, you win!\n\nMultiple decks of Star Realms and/or Star Realms: Colony Wars, one for every two people, allows up to six players to play a variety of scenarios. Also, in the newest version, there are new ways to play that allow up to 6 players with modes like Boss, Hunter, and Free for All. You can also add Star Realms Colony Wars to the deck to make it 4 players. This is the first game of the Star Realms series.",
            "minPlayers": 2,
            "maxPlayers": 2,
            "winMethod": "individual-score",
            "imageLink": "https://cf.geekdo-images.com/EsJqPL5CB_TMt0MYL-lnVg__original/img/QXgamCDRuBoRJyU1PQjeh58Pvr8=/0x0/filters:format(jpeg)/pic1903816.jpg",
            "links": [
                {
                    "type": "board-game-geek",
                    "link": "https://boardgamegeek.com/boardgame/147020/star-realms"
                },
                {
                    "type": "official-website",
                    "link": "https://www.starrealms.com/"
                }
            ]
        },
    ]

    return games

def get_groups():
    groups = [
        {
            "id": "120a6b3b-f519-4873-b04a-9e96b65c4280",
            "name": "test-group",
            "timeCreated": 1659775919,
            "type": "public",
            "displayName": "Test Group",
            "description": "A test group",
        },
    ]

    return groups

def get_link_types():
    link_types = [
        {
            "id": "dd7265f2-44b4-4b96-9a9c-c2d7c84025c1",
            "name": "board-game-geek",
            "timeCreated": 1659777659,
            "displayName": "BoardGameGeek"
        },
    ]

    return link_types

def get_players():
    players = [
        {
            "id": "625b90d9-a918-4e91-b2ff-db16c48d828d",
            "username": "julianl",
            "timeCreated": 1659775610,
            "displayName": "Julian Lawrance",
            "profilePicture": "https://e.snmc.io/i/600/s/9f6d3d17acac6ce20993eb158c203e4b/5662600/godspeed-you-black-emperor-lift-yr-skinny-fists-like-antennas-to-heaven-cover-art.jpg"
        },
    ]

    return players

def get_results():
    results = [
        {
            "id": "c919e7d0-19ab-46f7-a92a-f99b373dfae7",
            "gameName": "star-realms",
            "groupName": "all",
            "timeCreated": 1659776889,
            "timePlayed": 1659776828,
            "notes": "Burning Vipers and Scouts from my deck gives you so much more",
            "cooperativeScore": 0,
            "cooperativeWin": False,
            "scores": [
                {
                    "username": "julianl",
                    "score": 14,
                    "isWinner": False
                },
                {
                    "username": "brianeno",
                    "score": 0,
                    "isWinner": False
                }
            ]
        },
    ]

    return results

def get_win_methods():
    win_methods = [
        {
            "id": "585c84cd-0e0a-485f-9415-d30c5cfc2fc3",
            "name": "individual-score",
            "timeCreated": 1659777803,
            "displayName": "Individual Score"
        },
    ]

    return win_methods
