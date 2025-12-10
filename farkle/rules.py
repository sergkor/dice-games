from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'FARKLE RULES & REFERENCE', 0, 1, 'C')
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

def create_farkle_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)

    # OBJECTIVE
    pdf.chapter_title('OBJECTIVE')
    pdf.chapter_body('Be the first player to score 10,000 points.')

    # ON YOUR TURN
    pdf.chapter_title('ON YOUR TURN')
    pdf.set_font('Arial', '', 10)
    
    steps = [
        ("1. Roll", "Roll all 6 dice."),
        ("2. Set Aside", "You MUST set aside at least one scoring die (or combination) to bank points for the turn."),
        ("3. Decide", "STOP: End turn and bank points.\nROLL AGAIN: Re-roll remaining dice to score more."),
        ("4. Farkle", "If you roll and have NO scoring dice, you FARKLE. You lose all accumulated points for that turn.")
    ]
    
    for title, desc in steps:
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(30, 5, title + ":", 0, 0)
        pdf.set_font('Arial', '', 10)
        pdf.multi_cell(0, 5, desc)
        pdf.ln(1)
    
    pdf.ln(1)

    # HOT DICE
    pdf.chapter_title('HOT DICE')
    pdf.chapter_body('If you set aside ALL 6 dice (over one or multiple rolls), you have "Hot Dice". You may roll all 6 dice again to accumulate more points. If you Farkle after rolling Hot Dice, you lose everything for that turn.')

    # SCORING COMBINATIONS
    pdf.chapter_title('SCORING COMBINATIONS')
    pdf.set_font('Arial', 'I', 9)
    pdf.cell(0, 5, 'Combinations must be rolled in a single throw. You cannot combine dice from different rolls.', 0, 1)
    pdf.ln(2)

    # Table Header
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(80, 6, 'Dice Combination', 1)
    pdf.cell(40, 6, 'Score', 1, 1)
    
    # Table Body
    pdf.set_font('Arial', '', 10)
    data = [
        ('Single 5', '50'),
        ('Single 1', '100'),
        ('Three 1s', '300'),
        ('Three 2s', '200'),
        ('Three 3s', '300'),
        ('Three 4s', '400'),
        ('Three 5s', '500'),
        ('Three 6s', '600'),
        ('Four of a Kind', '1,000'),
        ('Five of a Kind', '2,000'),
        ('Six of a Kind', '3,000'),
        ('Straight (1-6)', '1,500'),
        ('Three Pairs', '1,500'),
        ('Two Triplets', '2,500'),
        ('Four of a Kind + A Pair', '1,500'),
    ]
    
    for combo, score in data:
        pdf.cell(80, 6, combo, 1)
        pdf.cell(40, 6, score, 1, 1)
    
    pdf.ln(2)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 5, '*Scoring rules vary by house. Agree on values before playing!', 0, 1)
    pdf.ln(3)

    # WINNING
    pdf.chapter_title('WINNING THE GAME')
    pdf.set_font('Arial', '', 10)
    pdf.cell(5, 5, '1.', 0, 0)
    pdf.multi_cell(0, 5, 'The End: When a player reaches 10,000 points, the "Last Chance" round begins.')
    pdf.cell(5, 5, '2.', 0, 0)
    pdf.multi_cell(0, 5, 'Last Chance: Every other player gets one final turn to beat the high score.')
    pdf.cell(5, 5, '3.', 0, 0)
    pdf.multi_cell(0, 5, 'The player with the highest score after the Last Chance round wins.')
    
    pdf.output('farkle-rules.pdf')

create_farkle_pdf()