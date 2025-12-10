from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'YAHTZEE RULES & REFERENCE', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, label, 0, 1, 'L', 1)
        self.ln(2)

    def chapter_body(self, txt):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, txt)
        self.ln()

def create_yahtzee_pdf_v2():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)

    # OBJECTIVE
    pdf.chapter_title('OBJECTIVE')
    pdf.chapter_body('Score the most points by rolling 5 dice to make specific combinations over 13 rounds.')

    # ON YOUR TURN
    pdf.chapter_title('ON YOUR TURN')
    pdf.set_font('Arial', '', 10)
    pdf.cell(10, 5, '1.', 0, 0)
    pdf.multi_cell(0, 5, 'Roll 1: Roll all 5 dice. Keep any you want to save; re-roll the rest.')
    pdf.cell(10, 5, '2.', 0, 0)
    pdf.multi_cell(0, 5, 'Roll 2: Re-roll any or all dice (even those you kept previously).')
    pdf.cell(10, 5, '3.', 0, 0)
    pdf.multi_cell(0, 5, 'Roll 3: Final re-roll of any or all dice.')
    pdf.cell(10, 5, '4.', 0, 0)
    pdf.multi_cell(0, 5, 'Score: You MUST fill in one box on your scorecard. If you cannot meet the requirements for a box, you must take a "0" in an empty box.')
    pdf.ln(3)

    # SCORING - UPPER
    pdf.chapter_title('UPPER SECTION SCORING')
    pdf.set_font('Arial', 'I', 9)
    pdf.cell(0, 5, 'Goal: Get a total score of at least 63 in this section to earn a 35-point Bonus.', 0, 1)
    pdf.ln(2)
    
    # Table Header
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(40, 6, 'Category', 1)
    pdf.cell(80, 6, 'Requirement', 1)
    pdf.cell(40, 6, 'Score', 1, 1)
    
    # Table Body
    pdf.set_font('Arial', '', 10)
    data_upper = [
        ('Aces (Ones)', 'At least one 1', 'Sum of all 1s'),
        ('Twos', 'At least one 2', 'Sum of all 2s'),
        ('Threes', 'At least one 3', 'Sum of all 3s'),
        ('Fours', 'At least one 4', 'Sum of all 4s'),
        ('Fives', 'At least one 5', 'Sum of all 5s'),
        ('Sixes', 'At least one 6', 'Sum of all 6s'),
    ]
    for cat, req, score in data_upper:
        pdf.cell(40, 6, cat, 1)
        pdf.cell(80, 6, req, 1)
        pdf.cell(40, 6, score, 1, 1)
    pdf.ln(5)

    # SCORING - LOWER
    pdf.chapter_title('LOWER SECTION SCORING')
    
    # Table Header
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(40, 6, 'Category', 1)
    pdf.cell(80, 6, 'Requirement', 1)
    pdf.cell(40, 6, 'Score', 1, 1)
    
    # Table Body
    pdf.set_font('Arial', '', 10)
    data_lower = [
        ('3 of a Kind', 'At least 3 dice same face', 'Sum of ALL 5 dice'),
        ('4 of a Kind', 'At least 4 dice same face', 'Sum of ALL 5 dice'),
        ('Full House', '3 of one number, 2 of another', '25 Points'),
        ('Small Straight', '4 sequential numbers', '30 Points'),
        ('Large Straight', '5 sequential numbers', '40 Points'),
        ('Yahtzee', '5 dice of the same face', '50 Points'),
        ('Chance', 'Any combination', 'Sum of ALL 5 dice'),
    ]
    for cat, req, score in data_lower:
        pdf.cell(40, 6, cat, 1)
        pdf.cell(80, 6, req, 1)
        pdf.cell(40, 6, score, 1, 1)
    pdf.ln(5)

    # BONUSES
    pdf.chapter_title('YAHTZEE BONUS & JOKER RULES')
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'If you roll a Yahtzee and your "Yahtzee" box is ALREADY filled with 50:')
    pdf.set_font('Arial', '', 10)
    pdf.cell(10, 5, '-', 0, 0, 'R')
    pdf.multi_cell(0, 5, 'Mark 100 bonus points in the bonus section.')
    pdf.cell(10, 5, '-', 0, 0, 'R')
    pdf.multi_cell(0, 5, 'Joker Rule: You must also fill a scoring box for this turn. First, try to fill the corresponding number in the Upper Section. If that is full, you may fill ANY open box in the Lower Section (for full points).')
    
    # ADDED NOTE HERE
    pdf.ln(2)
    pdf.set_font('Arial', 'BI', 9)
    pdf.multi_cell(0, 5, 'NOTE: If your original Yahtzee box was filled with a 0, you do NOT get the 100 point bonus, but you must still follow the Joker Rule.')
    pdf.ln(3)

    # GAME END
    pdf.chapter_title('GAME END')
    pdf.chapter_body('The game ends after 13 rounds when all boxes are filled.\nTotal Score = Upper Total + Upper Bonus (if >63) + Lower Total + Yahtzee Bonuses.')

    pdf.output('yahtzee_rules_card_v2.pdf')

create_yahtzee_pdf_v2()