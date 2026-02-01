print("🧠 AI Behavior Pattern Analyzer \n")

sleep = float(input("Sleep hours: "))
work = float(input("Work hours: "))
exercise = int(input("Exercise minutes: "))
screen = float(input("Screen time hours: "))

print("\n📊 BEHAVIOR ANALYSIS")

if sleep >= 7:
    print("😴 Sleep Pattern: Healthy")
else:
    print("⚠️ Sleep Pattern: Poor")

if work <= 8:
    print("💼 Work Pattern: Balanced")
else:
    print("⚠️ Work Pattern: Overworking")

if exercise >= 30:
    print("🏃 Exercise Pattern: Active")
else:
    print("⚠️ Exercise Pattern: Inactive")

if screen <= 4:
    print("📱 Screen Usage: Controlled")
else:
    print("⚠️ Screen Usage: Excessive")

print("\n🧭 AI Behavioral Advice")

if sleep < 7:
    print("• Improve sleep routine")
if work > 8:
    print("• Reduce workload")
if exercise < 30:
    print("• Increase physical activity")
if screen > 4:
    print("• Limit screen time")
