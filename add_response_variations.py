#!/usr/bin/env python3
"""Add multiple response variations to existing anchors"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.anchor_manager import AnchorManager, SemanticAnchor

def add_variations(manager):
    """Add response variations to existing anchors"""
    
    variations = {
        "prac_beginner": [
            "Starting something new takes courage. What's one thing you're curious about?",
            "Everyone was a beginner once. What's the smallest step you can take?",
            "What would make this feel more approachable for you?"
        ],
        "prac_overwhelmed": [
            "When everything feels urgent, nothing is. What's the one thing that matters most?",
            "Let's simplify. What's the core thing you need right now?",
            "Your brain needs space. What can we set aside for now?"
        ],
        "prac_frustrated": [
            "Frustration means you care. What's the part that's most frustrating?",
            "Sometimes stepping away helps. What if you took a breath?",
            "What's one thing you've learned from this?"
        ],
        "career_imposter": [
            "That voice is loud, but it's not telling the truth. What evidence do you have that you belong?",
            "If a friend felt this way, what would you tell them?",
            "Almost everyone feels this sometimes. What's one thing you know you're good at?"
        ],
        "career_anxiety": [
            "That gap of time can feel enormous. What's one skill you're proud of?",
            "You've navigated change before. What helped then?",
            "What's the part that feels most unfamiliar?"
        ],
        "career_burnout": [
            "Burnout is real. What's one thing that would give you relief?",
            "You've been giving so much. What would it look like to receive?",
            "Rest isn't earned. What would real rest look like?"
        ],
        "rel_betrayal": [
            "Trust broken is profound. What do you need to feel safe again?",
            "That kind of hurt takes time. What's one thing you can do for yourself right now?",
            "What would you want them to understand about how this affected you?"
        ],
        "rel_conflict": [
            "Conflict is heavy. What's underneath the anger?",
            "What would you want them to hear if they could really listen?",
            "What's the one thing you need right now?"
        ],
        "rel_loss": [
            "Loss of connection is a unique grief. What do you miss most?",
            "Some relationships have seasons. What did this one teach you?",
            "What would you want to carry forward?"
        ],
        "exist_diagnosis": [
            "A diagnosis changes everything. What's most present for you in this moment?",
            "You don't have to figure it all out today. What's one thing you want to know?",
            "This is a lot to hold. What do you need right now?"
        ],
        "exist_identity": [
            "Losing your sense of self is disorienting. What did you used to know about yourself?",
            "You're still in there. What's one thing that's always been you?",
            "What feels like it's still true?"
        ],
        "phil_emptiness": [
            "Emptiness isn't depression. It's a question waiting for an answer. What did you want before you had everything?",
            "Sometimes emptiness is space for what's next. What's trying to emerge?",
            "What would fill you, even a little?"
        ],
        "phil_despair": [
            "That weight is real. You don't have to carry it alone.",
            "Hopelessness is exhausting. What's one small thing that still matters?",
            "When everything feels dark, even a small light matters. What's flickering?"
        ],
        "phil_meaning": [
            "That question can't be answered—it has to be lived. What matters enough to carry without certainty?",
            "Meaning is found in the living, not the finding. What are you paying attention to?",
            "What would make this feel meaningful, even if just for today?"
        ]
    }
    
    count = 0
    for anchor_id, new_responses in variations.items():
        anchor = manager.get_anchor(anchor_id)
        if anchor:
            existing = anchor.responses
            combined = existing + new_responses
            anchor.responses = combined[:6]  # Keep max 6 responses
            manager.add_anchor(anchor)
            print(f"✅ Updated {anchor_id} with {len(new_responses)} new responses")
            count += 1
        else:
            print(f"⚠️ Anchor {anchor_id} not found")
    
    return count

if __name__ == "__main__":
    manager = AnchorManager()
    print(f"Current anchors: {len(manager.anchors)}")
    count = add_variations(manager)
    print(f"\n✅ Updated {count} anchors with new responses")
    print(f"Total anchors: {len(manager.anchors)}")
