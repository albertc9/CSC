import ROOT
h = ROOT.TH1F("h1", "Test Histogram", 100, -3, 3)
h.FillRandom("gaus", 10000)
h.Draw()
print("ROOT histogram created and drawn successfully.")