from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import Qt

from core.utils import RoughTime
from core.conf import conf
import math


class ProgressBar(QProgressBar):
  def __init__(self, id, tmpl):
    super(ProgressBar, self).__init__()
    self.id = id
    self.tmpl = tmpl

    self.setOrientation(Qt.Horizontal)
    self.setRange(0, 100)
    self.setValue(0)

  def Max(self):
    return self.game[self.id]["max"]

  def Position(self):
    return self.game[self.id]["position"]

  def reset(self, newmax, newposition = None):
    self.game[self.id]["max"] = newmax
    self.reposition(newposition or 0)

  def reposition(self, newpos):
    self.game[self.id]["position"] = min([newpos, self.Max()])
    self.game[self.id]["percent"] = 100 * self.Position() // self.Max() if self.Max() else 0
    self.game[self.id]["remaining"] = math.floor(self.Max() - self.Position())
    self.game[self.id]["time"] = RoughTime(self.Max() - self.Position())
    self.game[self.id]["hint"] = conf.template(self.tmpl, self.game[self.id])

    p = round(100 * self.Position() / self.Max() if self.Max() else 0)
    self.setValue(p)

  def increment(self, inc):
    self.reposition(self.Position() + inc)

  def done(self):
    return self.Position() >= self.Max()

  def load(self, game):
    self.game = game
    self.reposition(self.Position())