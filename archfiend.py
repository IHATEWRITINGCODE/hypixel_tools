import random

ARCHFIEND_DICE_COST = 3.5e7
ROLL_COST = 6.6e6
ARCHFIEND_DYE_VALUE = 5e7
ARCHFIEND_PRIZE_AMOUNT = 1e8
STARTING_BANKROLL = 1e9
DYE_COUNT = 0

def dice_roll():
    random_number = random.randrange(1, 666)
    if random_number == 1:
        return True, ARCHFIEND_DYE_VALUE, "Dye"
    
    random_number = random.randrange(1, 16)
    if random_number == 1:
        return True, ARCHFIEND_PRIZE_AMOUNT, "Prize"
    
    else:
        return False, 0, ""

if __name__ == "__main__":
    print(f"Starting with ${int(STARTING_BANKROLL):,}...")
    purse = STARTING_BANKROLL
    max_purse = min_purse = purse
    bankrupted = False
    
    for dice in range(10):
        if purse >= ARCHFIEND_DICE_COST:
            purse -= ARCHFIEND_DICE_COST
            print(f"\nPurchasing dice... New purse is ${int(purse):,}")
        else:
            print(f"\Can't afford archfiend dice! Purse has fallen to ${int(purse):,}")
            bankrupted = True
            break
        
        losing = True
        attempts = 0
        initial_purse = purse
        
        while losing:
            if purse >= ROLL_COST:
                purse -= ROLL_COST
                roll_status, roll_amount, roll_outcome = dice_roll()
            else:
                print(
                    f"\nBankrupted! Can't afford to roll the dice! Purse is ${int(purse):,}\n"
                    f"On this dice, you went {attempts} attempts without a prize!\n"
                    f"This consumed ${int(attempts * ROLL_COST):,} "
                    f"from your initial ${int(initial_purse):,} purse!"
                )
                bankrupted = True
                break
            
            attempts += 1
            purse += roll_amount
            if purse > max_purse: max_purse = purse
            if purse < min_purse: min_purse = purse
            if roll_outcome == "Dye": DYE_COUNT += 1
            
            if roll_status:
                losing = False
        
        if not bankrupted:
            delta = purse - initial_purse
            print(
                f"Dice {dice + 1}:",
                    f"\t- {roll_outcome} awarded",
                    f"\t- {attempts} attempts",
                    f"\t- start: ${int(initial_purse):,}",
                    f"\t- dropped to: ${int(initial_purse - attempts * ROLL_COST):,}",
                    f"\t- end: ${int(purse):,}",
                    f"\t- +${int(delta):,} profit!" if delta > 0 else f"\t- -${int(abs(delta)):,} loss...",
                sep='\n'
            )
    
    print(f"\nOverall change in purse: {int(purse - STARTING_BANKROLL):+,}")
    print(f"\t- Highest point: ${int(max_purse):,}")
    print(f"\t- Lowest point: ${int(min_purse):,}")
    if DYE_COUNT: print(f"\t- Got {DYE_COUNT} dye(s)...")
