from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_CENTER

OUTPUT = "AI_Engineering_Workflow_General_Audience.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=1.1 * inch,
    rightMargin=1.1 * inch,
    topMargin=1.0 * inch,
    bottomMargin=1.0 * inch,
    title="AI Engineering Workflow - Where AI Chats Become Project Records",
    author="John Colby",
)

styles = getSampleStyleSheet()
DARK = colors.HexColor("#1a1a1a")
ACCENT = colors.HexColor("#2c5f8a")
RULE = colors.HexColor("#cccccc")

title_style = ParagraphStyle("DocTitle", parent=styles["Title"],
    fontSize=22, leading=28, textColor=ACCENT, spaceAfter=4,
    fontName="Helvetica-Bold", alignment=TA_CENTER)
subtitle_style = ParagraphStyle("DocSubtitle", parent=styles["Normal"],
    fontSize=13, leading=18, textColor=DARK, spaceAfter=20,
    fontName="Helvetica-Oblique", alignment=TA_CENTER)
h2_style = ParagraphStyle("H2", parent=styles["Heading2"],
    fontSize=13, leading=18, textColor=ACCENT,
    spaceBefore=18, spaceAfter=6, fontName="Helvetica-Bold")
body_style = ParagraphStyle("Body", parent=styles["Normal"],
    fontSize=10.5, leading=16, textColor=DARK, spaceAfter=8, fontName="Helvetica")
bullet_style = ParagraphStyle("Bullet", parent=body_style, leftIndent=18, spaceAfter=4)
step_style = ParagraphStyle("Step", parent=body_style, leftIndent=18, spaceAfter=3)
quote_style = ParagraphStyle("Quote", parent=body_style,
    fontSize=10.5, leading=16, fontName="Helvetica-BoldOblique",
    textColor=DARK, spaceAfter=8)
byline_style = ParagraphStyle("Byline", parent=body_style,
    fontSize=10, textColor=colors.HexColor("#555555"), spaceBefore=24, spaceAfter=4)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=RULE, spaceAfter=14, spaceBefore=6)
def h2(text):
    return Paragraph(text, h2_style)
def body(text):
    return Paragraph(text, body_style)
def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, bullet_style), bulletColor=ACCENT) for i in items],
        bulletType="bullet", leftIndent=18, bulletFontSize=8, spaceAfter=8)
def numbered(items):
    return ListFlowable(
        [ListItem(Paragraph(i, step_style)) for i in items],
        bulletType="1", leftIndent=18, bulletFontSize=10, spaceAfter=8)

story = []

story.append(Paragraph("AI Engineering Workflow", title_style))
story.append(Paragraph("Where AI Chats Become Project Records", subtitle_style))
story.append(hr())

story.append(body("AI can help you think faster than any tool most of us have ever used."))
story.append(body(
    "It can help shape an idea, challenge assumptions, draft a plan, write copy, and find "
    "problems you did not know to look for. But there is a catch: the useful work often "
    "lives inside a chat transcript."
))
story.append(body("That feels fine while the conversation is active. It feels much worse later."))
story.append(body(
    "You come back to a long thread and try to remember which version of the idea was best. "
    "You scroll past abandoned branches, half-decisions, useful objections, and paragraphs "
    "that felt brilliant at the time but are now hard to place. If you used more than one AI "
    "tool, the problem gets worse: you become the copy/paste bridge between systems."
))
story.append(body("AI Engineering Workflow exists to solve that problem."))
story.append(body(
    "It turns AI-assisted work into a durable record: what was proposed, what was challenged, "
    "what changed, what was approved, and what should happen next."
))
story.append(body(
    "<b>The point is not to make AI autonomous. The point is to make AI collaboration legible.</b>"
))
story.append(hr())

story.append(h2("The Core Idea"))
story.append(body(
    "AI Engineering Workflow is a simple discipline: keep the important parts of your AI "
    "work in a structured record outside the chat."
))
story.append(body("Chat is the workspace. The record is the durable state."))
story.append(body("At a high level:"))
story.append(numbered([
    "You define the objective.",
    "An AI proposes.",
    "A second perspective critiques - another AI, a trusted colleague, or your own structured review.",
    "You clarify priorities and stay the final authority.",
    "The proposal is revised.",
    "The scope is agreed on before work begins.",
    "You approve the next step.",
    "Work proceeds.",
    "Results are validated against what was agreed.",
]))
story.append(body(
    "This is familiar discipline applied to AI-assisted work: proposal, critique, revision, "
    "approval, execution, validation. Nothing exotic. Just written down."
))
story.append(hr())

story.append(h2("What Problem It Solves"))
story.append(body(
    "Ordinary AI chat has a hidden failure mode: it feels productive while the session is "
    "active, but the useful structure evaporates."
))
story.append(body("Common symptoms:"))
story.append(bullets([
    "Good ideas get buried in long transcripts.",
    "Decisions blur together with speculation.",
    "Critiques get softened or lost when you switch tools.",
    "Scope changes silently.",
    "A later session has no reliable state to resume from.",
    "You spend more time recovering the work than doing it.",
]))
story.append(body(
    "AI Engineering Workflow moves the important state out of chat and into a structured record."
))
story.append(body("That simple shift changes the work."))
story.append(body(
    "Instead of asking \"what did we decide somewhere in that thread?\" the record says what "
    "was proposed, what objections were raised, what changed, what is approved, and what "
    "remains open."
))
story.append(hr())

story.append(h2("The Second Perspective"))
story.append(body(
    "One of the most useful moves in this workflow is getting a second perspective before "
    "committing to a direction."
))
story.append(body(
    "When you use a single AI for both generating and reviewing an idea, you often get "
    "agreement. The same system that produced the answer is evaluating it. It tends to "
    "confirm what it already said."
))
story.append(body(
    "A second perspective - another AI tool, a colleague, or your own structured review "
    "pass - creates useful friction. It makes disagreement cheaper. It surfaces problems "
    "before they become expensive."
))
story.append(body(
    "In the full workflow, two AI tools are used: one to propose, one to critique. But the "
    "principle applies at any level of tooling. Even asking a different AI a pointed question "
    "about your plan before committing to it is more valuable than asking the same one to "
    "check its own work."
))
story.append(body(
    "The human stays in authority. The AI systems are reasoning tools inside a governed "
    "process. They are not the decision-makers."
))
story.append(hr())

story.append(h2("The Workflow Record"))
story.append(body("The Workflow Record is the center of the system."))
story.append(body(
    "It is a plain text file that captures:"
))
story.append(bullets([
    "what you are trying to accomplish",
    "what was proposed",
    "what concerns were raised",
    "how those concerns were resolved",
    "what scope was agreed on",
    "who approved the next step",
    "what validation is required",
]))
story.append(body("The rule is simple:"))
story.append(Paragraph(
    ""If a decision is not in the Workflow Record, it did not happen in any durable sense."",
    quote_style
))
story.append(body(
    "This makes the record useful to you, to future AI sessions, and to anyone else trying "
    "to understand how a decision was reached. The format is intentionally plain so it works "
    "across any AI tool, any device, and any future system."
))
story.append(hr())

story.append(h2("Keeping Scope Under Control"))
story.append(body(
    "AI tools are very good at expanding scope. They add useful-looking features, alternate "
    "framings, and extra cases. Sometimes that is helpful. Often it causes drift."
))
story.append(body(
    "The workflow addresses this with a scope freeze: before work begins, the agreed scope "
    "is written down explicitly - including what is out of scope."
))
story.append(body(
    "This prevents the quiet accumulation of unreviewed additions. It also makes it easier "
    "to say \"that's a good idea, but it belongs in a later record\" rather than letting "
    "the current work grow without bound."
))
story.append(hr())

story.append(h2("What This Is Not"))
story.append(body("AI Engineering Workflow is not:"))
story.append(bullets([
    "a prompt collection",
    "a fully automated agent system",
    "a replacement for human judgment",
    "a claim that AI output is automatically correct",
    "a tool for teams at scale (not yet tested at that level)",
]))
story.append(body(
    "It is a practical discipline for making AI-assisted work easier to review, resume, and "
    "trust - whether you are a builder, a writer, an entrepreneur, or anyone else using AI "
    "to turn ideas into real projects."
))
story.append(hr())

story.append(h2("A Simple Example"))
story.append(body("<b>Without the workflow:</b>"))
story.append(body(
    "You brainstorm with an AI for an hour. The conversation is productive. Later, you try "
    "to recover the useful parts from the transcript. You remember there was a good objection "
    "somewhere, a better version of the idea, and a decision about scope - but now it is all "
    "mixed together."
))
story.append(body("<b>With the workflow:</b>"))
story.append(body(
    "The proposal goes into the record. The critique goes into the record. Your clarification "
    "goes into the record. The agreed scope and next action are explicit."
))
story.append(body(
    "The conversation still happens, but the work no longer disappears into the conversation."
))
story.append(hr())

story.append(h2("Why It Matters"))
story.append(body("AI-assisted work is moving from quick answers toward real projects."))
story.append(body(
    "Real projects need memory, review, state, and approval. They need a way to know what "
    "has been decided and what has not. They need a way to resume after a tool switch, a "
    "context reset, or a day away."
))
story.append(body(
    "AI Engineering Workflow gives that process a simple form: plain text records, explicit "
    "roles, a second perspective, scope agreement, and human approval before work proceeds."
))
story.append(body("It is not heavy machinery. It is a way to stop treating chat as the project record."))
story.append(hr())

story.append(h2("Current Status"))
story.append(body("The workflow is public and documented at:"))
story.append(Paragraph(
    '<a href="https://github.com/jwcolby54/AI_Engineering_Workflow_Wiki" color="#2c5f8a">'
    'https://github.com/jwcolby54/AI_Engineering_Workflow_Wiki</a>', body_style))
story.append(body(
    "It is currently tested as a solo-human workflow. A natural next step would be broader "
    "use across more tools, more domains, and eventually more people in the loop."
))
story.append(hr())

story.append(Paragraph("John Colby", byline_style))
story.append(Paragraph("Builder of AI-assisted systems and author of AI Engineering Workflow.",
    ParagraphStyle("BylineDetail", parent=byline_style, spaceAfter=2)))
story.append(Paragraph(
    '<a href="https://github.com/jwcolby54/AI_Engineering_Workflow_Wiki" color="#2c5f8a">'
    'github.com/jwcolby54/AI_Engineering_Workflow_Wiki</a>',
    ParagraphStyle("BylineLink", parent=byline_style, spaceAfter=2)))
story.append(Paragraph(
    '<a href="https://www.linkedin.com/in/john-colby-1625b95/" color="#2c5f8a">'
    'linkedin.com/in/john-colby-1625b95</a>',
    ParagraphStyle("BylineLinkedIn", parent=byline_style, spaceAfter=0)))

doc.build(story)
print(f"PDF written to {OUTPUT}")
