import pytest
from project import Madrassah,Player  # Import your Madrassah class from your code

# Initialize a Madrassah object for testing
@pytest.fixture
def madrassah():
    return Madrassah()

# Initialize a Player object for testing
@pytest.fixture
def player():
    return Player()

def test_generate_npcs(player):
    num_npcs = 5  # Test with 5 NPCs
    player.num_npcs = num_npcs
    npcs = player.generate_npcs()

    assert len(npcs) == num_npcs  # Check if the correct number of NPCs is generated
    for npc in npcs:
        assert isinstance(npc, dict)
        assert 'name' in npc
        assert 'relationship' in npc
        assert npc['name'] in player.male or npc['name'] in player.female
        assert 1 <= npc['relationship'] <= 100  # Relationship should be within this range

def test_randomize_names(player):
    original_male_names = player.male.copy()
    original_female_names = player.female.copy()

    player.randomize_names()

    # Check if shuffling the names resulted in a different order
    assert sorted(player.male) != sorted(original_male_names)
    assert sorted(player.female) != sorted(original_female_names)

def test_purchase_item(player):
    item = {
        "name": "Test Item",
        "type": "Test Type",
        "price": 50,
        "attribute_effect": "test_attribute",
        "prestige_effect": 10
    }
    initial_gold = player.gold

    player.purchase_item(item, player)

    # Check if the player's gold is updated correctly after purchasing the item
    assert player.gold == initial_gold - item["price"]

    # Check if the player's inventory contains the purchased item
    assert any(i == item for i in player.inventory)

def test_meets_requirements(player):
    gig = {
        "name": "Test Gig",
        "requirements": {"test_stat": 10}
    }

    # Test when the player meets the gig requirements
    player.character.stats["test_stat"] = 15
    assert player.meets_requirements(gig) is True

    # Test when the player does not meet the gig requirements
    player.character.stats["test_stat"] = 5
    assert player.meets_requirements(gig) is False

def test_visit_marketplace(player, capsys, monkeypatch):
    # Mock user input to select an item for purchase
    user_input = ["1", "0"]

    # Mock the input function to simulate user input
    def mock_input(prompt):
        return user_input.pop(0)

    # Override the input function with the mock function
    monkeypatch.setattr('builtins.input', mock_input)

    # Initialize some test items in the marketplace
    player.items = [
        {"name": "Test Item 1", "type": "Type A", "price": 20},
        {"name": "Test Item 2", "type": "Type B", "price": 30}
    ]

    # Initialize player's gold
    player.gold = 100

    # Call the visit_marketplace method
    player.visit_marketplace(player)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the menu is displayed and the item is purchased
    assert "Welcome to the Ottoman Marketplace. What would you like to purchase?" in captured.out
    assert "Enter the number of the item you want to purchase: " in captured.out
    assert "You have purchased the Test Item 1 for 20 gold." in captured.out
    assert "Your inventory is empty." in captured.out  # Since we purchased an item, the inventory is not empty