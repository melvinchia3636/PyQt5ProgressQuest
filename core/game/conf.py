__all__ = ['conf']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['LevelUpTime', 'Pick', 'tabulate', 'seed', 'Mash', 'GenerateName', 'KParts', 'Random', 'template', 'K', 'randseed', 'Alea'])
@Js
def PyJsHoisted_tabulate_(list, this, arguments, var=var):
    var = Scope({'list':list, 'this':this, 'arguments':arguments}, var)
    var.registers(['list', 'result'])
    var.put('result', Js(''))
    @Js
    def PyJs_anonymous_0_(v, this, arguments, var=var):
        var = Scope({'v':v, 'this':this, 'arguments':arguments}, var)
        var.registers(['v'])
        if (var.get('v').get('length')==Js(2.0)):
            if var.get('v').get('1').get('length'):
                var.put('result', ((((Js('   ')+var.get('v').get('0'))+Js(': '))+var.get('v').get('1'))+Js('\n')), '+')
        else:
            var.put('result', ((Js('   ')+var.get('v'))+Js('\n')), '+')
    PyJs_anonymous_0_._set_name('anonymous')
    var.get('list').callprop('forEach', PyJs_anonymous_0_)
    return var.get('result')
PyJsHoisted_tabulate_.func_name = 'tabulate'
var.put('tabulate', PyJsHoisted_tabulate_)
@Js
def PyJsHoisted_template_(tmpl, data, this, arguments, var=var):
    var = Scope({'tmpl':tmpl, 'data':data, 'this':this, 'arguments':arguments}, var)
    var.registers(['tmpl', 'data', 'brag'])
    @Js
    def PyJs_anonymous_2_(str, p1, this, arguments, var=var):
        var = Scope({'str':str, 'p1':p1, 'this':this, 'arguments':arguments}, var)
        var.registers(['dict', 'p1', 'str'])
        var.put('dict', var.get('data'))
        @Js
        def PyJs_anonymous_3_(v, this, arguments, var=var):
            var = Scope({'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v'])
            if var.get('dict').neg():
                return Js(True)
            if (var.get('v')==Js('___')):
                var.put('dict', var.get('tabulate')(var.get('dict')))
            else:
                var.put('dict', var.get('dict').get(var.get('v').callprop('replace', Js('_'), Js(' '))))
                if (var.get('dict',throw=False).typeof()==Js('').typeof()):
                    var.put('dict', var.get('dict').callprop('escapeHtml'))
            return var.get(u"null")
        PyJs_anonymous_3_._set_name('anonymous')
        var.get('p1').callprop('split', Js('.')).callprop('forEach', PyJs_anonymous_3_)
        if PyJsStrictEq(var.get('dict'),var.get('undefined')):
            var.put('dict', Js(''))
        return var.get('dict')
    PyJs_anonymous_2_._set_name('anonymous')
    var.put('brag', var.get('tmpl').callprop('replace', JsRegExp('/\\$([_A-Za-z.]+)/g'), PyJs_anonymous_2_))
    return var.get('brag')
PyJsHoisted_template_.func_name = 'template'
var.put('template', PyJsHoisted_template_)
@Js
def PyJsHoisted_Mash_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'mash'])
    var.put('n', Js(4022871197))
    @Js
    def PyJs_anonymous_4_(data, this, arguments, var=var):
        var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'data', 'i'])
        var.put('data', var.get('data').callprop('toString'))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('data').get('length')):
            var.put('n', var.get('data').callprop('charCodeAt', var.get('i')), '+')
            var.put('h', (Js(0.02519603282416938)*var.get('n')))
            var.put('n', PyJsBshift(var.get('h'),Js(0.0)))
            var.put('h', var.get('n'), '-')
            var.put('h', var.get('n'), '*')
            var.put('n', PyJsBshift(var.get('h'),Js(0.0)))
            var.put('h', var.get('n'), '-')
            var.put('n', (var.get('h')*Js(4294967296)), '+')
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return (PyJsBshift(var.get('n'),Js(0.0))*Js(2.3283064365386963e-10))
    PyJs_anonymous_4_._set_name('anonymous')
    var.put('mash', PyJs_anonymous_4_)
    var.get('mash').put('version', Js('Mash 0.9'))
    return var.get('mash')
PyJsHoisted_Mash_.func_name = 'Mash'
var.put('Mash', PyJsHoisted_Mash_)
@Js
def PyJsHoisted_Alea_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    @Js
    def PyJs_anonymous_5_(args, this, arguments, var=var):
        var = Scope({'args':args, 'this':this, 'arguments':arguments}, var)
        var.registers(['mash', 's2', 'c', 's0', 'i', 'random', 's1', 'args'])
        var.put('s0', Js(0.0))
        var.put('s1', Js(0.0))
        var.put('s2', Js(0.0))
        var.put('c', Js(1.0))
        if var.get('args').get('length').neg():
            var.put('args', Js([(+var.get('Date').create())]))
        var.put('mash', var.get('Mash')())
        var.put('s0', var.get('mash')(Js(' ')))
        var.put('s1', var.get('mash')(Js(' ')))
        var.put('s2', var.get('mash')(Js(' ')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('args').get('length')):
            var.put('s0', var.get('mash')(var.get('args').get(var.get('i'))), '-')
            if (var.get('s0')<Js(0.0)):
                var.put('s0', Js(1.0), '+')
            var.put('s1', var.get('mash')(var.get('args').get(var.get('i'))), '-')
            if (var.get('s1')<Js(0.0)):
                var.put('s1', Js(1.0), '+')
            var.put('s2', var.get('mash')(var.get('args').get(var.get('i'))), '-')
            if (var.get('s2')<Js(0.0)):
                var.put('s2', Js(1.0), '+')
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.put('mash', var.get(u"null"))
        @Js
        def PyJs_anonymous_6_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.put('t', ((Js(2091639.0)*var.get('s0'))+(var.get('c')*Js(2.3283064365386963e-10))))
            var.put('s0', var.get('s1'))
            var.put('s1', var.get('s2'))
            return var.put('s2', (var.get('t')-var.put('c', (var.get('t')|Js(0.0)))))
        PyJs_anonymous_6_._set_name('anonymous')
        var.put('random', PyJs_anonymous_6_)
        @Js
        def PyJs_anonymous_7_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (var.get('random')()*Js(4294967296))
        PyJs_anonymous_7_._set_name('anonymous')
        var.get('random').put('uint32', PyJs_anonymous_7_)
        @Js
        def PyJs_anonymous_8_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (var.get('random')()+(((var.get('random')()*Js(2097152))|Js(0.0))*Js(1.1102230246251565e-16)))
        PyJs_anonymous_8_._set_name('anonymous')
        var.get('random').put('fract53', PyJs_anonymous_8_)
        var.get('random').put('version', Js('Alea 0.9'))
        var.get('random').put('args', var.get('args'))
        @Js
        def PyJs_anonymous_9_(newstate, this, arguments, var=var):
            var = Scope({'newstate':newstate, 'this':this, 'arguments':arguments}, var)
            var.registers(['newstate'])
            if var.get('newstate'):
                var.put('s0', var.get('newstate').get('0'))
                var.put('s1', var.get('newstate').get('1'))
                var.put('s2', var.get('newstate').get('2'))
                var.put('c', var.get('newstate').get('3'))
            return Js([var.get('s0'), var.get('s1'), var.get('s2'), var.get('c')])
        PyJs_anonymous_9_._set_name('anonymous')
        var.get('random').put('state', PyJs_anonymous_9_)
        return var.get('random')
    PyJs_anonymous_5_._set_name('anonymous')
    return PyJs_anonymous_5_(var.get('Array').get('prototype').get('slice').callprop('call', var.get('arguments')))
PyJsHoisted_Alea_.func_name = 'Alea'
var.put('Alea', PyJsHoisted_Alea_)
@Js
def PyJsHoisted_Random_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n'])
    return (var.get('seed').callprop('uint32')%var.get('n'))
PyJsHoisted_Random_.func_name = 'Random'
var.put('Random', PyJsHoisted_Random_)
@Js
def PyJsHoisted_randseed_(set, this, arguments, var=var):
    var = Scope({'set':set, 'this':this, 'arguments':arguments}, var)
    var.registers(['set'])
    return var.get('seed').callprop('state', var.get('set'))
PyJsHoisted_randseed_.func_name = 'randseed'
var.put('randseed', PyJsHoisted_randseed_)
@Js
def PyJsHoisted_Pick_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('a').get(var.get('Random')(var.get('a').get('length')))
PyJsHoisted_Pick_.func_name = 'Pick'
var.put('Pick', PyJsHoisted_Pick_)
@Js
def PyJsHoisted_GenerateName_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['result', 'i'])
    var.put('result', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<=Js(5.0)):
        var.put('result', var.get('Pick')(var.get('KParts').get((var.get('i')%Js(3.0)))), '+')
        # update
        var.put('i',Js(var.get('i').to_number())+Js(1))
    return (var.get('result').callprop('charAt', Js(0.0)).callprop('toUpperCase')+var.get('result').callprop('slice', Js(1.0)))
PyJsHoisted_GenerateName_.func_name = 'GenerateName'
var.put('GenerateName', PyJsHoisted_GenerateName_)
@Js
def PyJsHoisted_LevelUpTime_(level, this, arguments, var=var):
    var = Scope({'level':level, 'this':this, 'arguments':arguments}, var)
    var.registers(['level'])
    return ((Js(20.0)*var.get('level'))*Js(60.0))
PyJsHoisted_LevelUpTime_.func_name = 'LevelUpTime'
var.put('LevelUpTime', PyJsHoisted_LevelUpTime_)
pass
@Js
def PyJs_anonymous_1_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").callprop('replace', JsRegExp('/&/g'), Js('&amp;')).callprop('replace', JsRegExp('/</g'), Js('&lt;')).callprop('replace', JsRegExp('/>/g'), Js('&gt;'))
PyJs_anonymous_1_._set_name('anonymous')
var.get('String').get('prototype').put('escapeHtml', PyJs_anonymous_1_)
pass
pass
pass
var.put('seed', var.get('Alea').create())
pass
pass
pass
var.put('KParts', Js([Js('br|cr|dr|fr|gr|j|kr|l|m|n|pr||||r|sh|tr|v|wh|x|y|z').callprop('split', Js('|')), Js('a|a|e|e|i|i|o|o|u|u|ae|ie|oo|ou').callprop('split', Js('|')), Js('b|ck|d|g|k|m|n|p|t|v|x|z').callprop('split', Js('|'))]))
pass
@Js
def PyJs_anonymous_10_(divisor, this, arguments, var=var):
    var = Scope({'divisor':divisor, 'this':this, 'arguments':arguments}, var)
    var.registers(['divisor', 'dividend'])
    var.put('dividend', (var.get(u"this")/var.get('divisor')))
    return (var.get('Math').get('ceil') if (var.get('dividend')<Js(0.0)) else var.get('Math').get('floor'))(var.get('dividend'))
PyJs_anonymous_10_._set_name('anonymous')
var.get('Number').get('prototype').put('div', PyJs_anonymous_10_)
pass
var.put('K', Js({}))
var.get('K').put('Traits', Js([Js('Name'), Js('Race'), Js('Class'), Js('Level')]))
var.get('K').put('PrimeStats', Js([Js('STR'), Js('CON'), Js('DEX'), Js('INT'), Js('WIS'), Js('CHA')]))
var.get('K').put('Stats', var.get('K').get('PrimeStats').callprop('slice', Js(0.0)).callprop('concat', Js([Js('HP Max'), Js('MP Max')])))
var.get('K').put('Equips', Js([Js('Weapon'), Js('Shield'), Js('Helm'), Js('Hauberk'), Js('Brassairts'), Js('Vambraces'), Js('Gauntlets'), Js('Gambeson'), Js('Cuisses'), Js('Greaves'), Js('Sollerets')]))
def PyJs_LONG_11_(var=var):
    return var.get('K').put('Spells', Js([Js('Slime Finger'), Js('Rabbit Punch'), Js('Hastiness'), Js('Good Move'), Js('Sadness'), Js('Seasick'), Js('Gyp'), Js('Shoelaces'), Js('Innoculate'), Js('Cone of Annoyance'), Js('Magnetic Orb'), Js('Invisible Hands'), Js('Revolting Cloud'), Js('Aqueous Humor'), Js('Spectral Miasma'), Js('Clever Fellow'), Js('Lockjaw'), Js('History Lesson'), Js('Hydrophobia'), Js('Big Sister'), Js('Cone of Paste'), Js('Mulligan'), Js("Nestor's Bright Idea"), Js('Holy Batpole'), Js('Tumor (Benign)'), Js('Braingate'), Js('Summon a Bitch'), Js('Nonplus'), Js('Animate Nightstand'), Js('Eye of the Troglodyte'), Js('Curse Name'), Js('Dropsy'), Js('Vitreous Humor'), Js("Roger's Grand Illusion"), Js('Covet'), Js('Black Idaho'), Js('Astral Miasma'), Js('Spectral Oyster'), Js('Acrid Hands'), Js('Angioplasty'), Js("Grognor's Big Day Off"), Js('Tumor (Malignant)'), Js('Animate Tunic'), Js('Ursine Armor'), Js('Holy Roller'), Js('Tonsilectomy'), Js('Curse Family'), Js('Infinite Confusion')]))
PyJs_LONG_11_()
var.get('K').put('OffenseAttrib', Js([Js('Polished|+1'), Js('Serrated|+1'), Js('Heavy|+1'), Js('Pronged|+2'), Js('Steely|+2'), Js('Vicious|+3'), Js('Venomed|+4'), Js('Stabbity|+4'), Js('Dancing|+5'), Js('Invisible|+6'), Js('Vorpal|+7')]))
var.get('K').put('DefenseAttrib', Js([Js('Studded|+1'), Js('Banded|+2'), Js('Gilded|+2'), Js('Festooned|+3'), Js('Holy|+4'), Js('Cambric|+1'), Js('Fine|+4'), Js('Impressive|+5'), Js('Custom|+3')]))
var.get('K').put('Shields', Js([Js('Parasol|0'), Js('Pie Plate|1'), Js('Garbage Can Lid|2'), Js('Buckler|3'), Js('Plexiglass|4'), Js('Fender|4'), Js('Round Shield|5'), Js('Carapace|5'), Js('Scutum|6'), Js('Propugner|6'), Js('Kite Shield|7'), Js('Pavise|8'), Js('Tower Shield|9'), Js('Baroque Shield|11'), Js('Aegis|12'), Js('Magnetic Field|18')]))
var.get('K').put('Armors', Js([Js('Lace|1'), Js('Macrame|2'), Js('Burlap|3'), Js('Canvas|4'), Js('Flannel|5'), Js('Chamois|6'), Js('Pleathers|7'), Js('Leathers|8'), Js('Bearskin|9'), Js('Ringmail|10'), Js('Scale Mail|12'), Js('Chainmail|14'), Js('Splint Mail|15'), Js('Platemail|16'), Js('ABS|17'), Js('Kevlar|18'), Js('Titanium|19'), Js('Mithril Mail|20'), Js('Diamond Mail|25'), Js('Plasma|30')]))
def PyJs_LONG_12_(var=var):
    return var.get('K').put('Weapons', Js([Js('Stick|0'), Js('Broken Bottle|1'), Js('Shiv|1'), Js('Sprig|1'), Js('Oxgoad|1'), Js('Eelspear|2'), Js('Bowie Knife|2'), Js('Claw Hammer|2'), Js('Handpeen|2'), Js('Andiron|3'), Js('Hatchet|3'), Js('Tomahawk|3'), Js('Hackbarm|3'), Js('Crowbar|4'), Js('Mace|4'), Js('Battleadze|4'), Js('Leafmace|5'), Js('Shortsword|5'), Js('Longiron|5'), Js('Poachard|5'), Js('Baselard|5'), Js('Whinyard|6'), Js('Blunderbuss|6'), Js('Longsword|6'), Js('Crankbow|6'), Js('Blibo|7'), Js('Broadsword|7'), Js('Kreen|7'), Js('Warhammer|7'), Js('Morning Star|8'), Js('Pole-adze|8'), Js('Spontoon|8'), Js('Bastard Sword|9'), Js('Peen-arm|9'), Js('Culverin|10'), Js('Lance|10'), Js('Halberd|11'), Js('Poleax|12'), Js('Bandyclef|15')]))
PyJs_LONG_12_()
def PyJs_LONG_13_(var=var):
    return var.get('K').put('Specials', Js([Js('Diadem'), Js('Festoon'), Js('Gemstone'), Js('Phial'), Js('Tiara'), Js('Scabbard'), Js('Arrow'), Js('Lens'), Js('Lamp'), Js('Hymnal'), Js('Fleece'), Js('Laurel'), Js('Brooch'), Js('Gimlet'), Js('Cobble'), Js('Albatross'), Js('Brazier'), Js('Bandolier'), Js('Tome'), Js('Garnet'), Js('Amethyst'), Js('Candelabra'), Js('Corset'), Js('Sphere'), Js('Sceptre'), Js('Ankh'), Js('Talisman'), Js('Orb'), Js('Gammel'), Js('Ornament'), Js('Brocade'), Js('Galoon'), Js('Bijou'), Js('Spangle'), Js('Gimcrack'), Js('Hood'), Js('Vulpeculum')]))
PyJs_LONG_13_()
def PyJs_LONG_14_(var=var):
    return var.get('K').put('ItemAttrib', Js([Js('Golden'), Js('Gilded'), Js('Spectral'), Js('Astral'), Js('Garlanded'), Js('Precious'), Js('Crafted'), Js('Dual'), Js('Filigreed'), Js('Cruciate'), Js('Arcane'), Js('Blessed'), Js('Reverential'), Js('Lucky'), Js('Enchanted'), Js('Gleaming'), Js('Grandiose'), Js('Sacred'), Js('Legendary'), Js('Mythic'), Js('Crystalline'), Js('Austere'), Js('Ostentatious'), Js('One True'), Js('Proverbial'), Js('Fearsome'), Js('Deadly'), Js('Benevolent'), Js('Unearthly'), Js('Magnificent'), Js('Iron'), Js('Ormolu'), Js('Puissant')]))
PyJs_LONG_14_()
def PyJs_LONG_15_(var=var):
    return var.get('K').put('ItemOfs', Js([Js('Foreboding'), Js('Foreshadowing'), Js('Nervousness'), Js('Happiness'), Js('Torpor'), Js('Danger'), Js('Craft'), Js('Silence'), Js('Invisibility'), Js('Rapidity'), Js('Pleasure'), Js('Practicality'), Js('Hurting'), Js('Joy'), Js('Petulance'), Js('Intrusion'), Js('Chaos'), Js('Suffering'), Js('Extroversion'), Js('Frenzy'), Js('Sisu'), Js('Solitude'), Js('Punctuality'), Js('Efficiency'), Js('Comfort'), Js('Patience'), Js('Internment'), Js('Incarceration'), Js('Misapprehension'), Js('Loyalty'), Js('Envy'), Js('Acrimony'), Js('Worry'), Js('Fear'), Js('Awe'), Js('Guile'), Js('Prurience'), Js('Fortune'), Js('Perspicacity'), Js('Domination'), Js('Submission'), Js('Fealty'), Js('Hunger'), Js('Despair'), Js('Cruelty'), Js('Grob'), Js('Dignard'), Js('Ra'), Js('the Bone'), Js('Diamonique'), Js('Electrum'), Js('Hydragyrum')]))
PyJs_LONG_15_()
def PyJs_LONG_16_(var=var):
    return var.get('K').put('BoringItems', Js([Js('nail'), Js('lunchpail'), Js('sock'), Js('I.O.U.'), Js('cookie'), Js('pint'), Js('toothpick'), Js('writ'), Js('newspaper'), Js('letter'), Js('plank'), Js('hat'), Js('egg'), Js('coin'), Js('needle'), Js('bucket'), Js('ladder'), Js('chicken'), Js('twig'), Js('dirtclod'), Js('counterpane'), Js('vest'), Js('teratoma'), Js('bunny'), Js('rock'), Js('pole'), Js('carrot'), Js('canoe'), Js('inkwell'), Js('hoe'), Js('bandage'), Js('trowel'), Js('towel'), Js('planter box'), Js('anvil'), Js('axle'), Js('tuppence'), Js('casket'), Js('nosegay'), Js('trinket'), Js('credenza'), Js('writ')]))
PyJs_LONG_16_()
def PyJs_LONG_17_(var=var):
    return var.get('K').put('Monsters', Js([Js('Anhkheg|6|chitin'), Js('Ant|0|antenna'), Js('Ape|4|ass'), Js('Baluchitherium|14|ear'), Js('Beholder|10|eyestalk'), Js('Black Pudding|10|saliva'), Js('Blink Dog|4|eyelid'), Js('Cub Scout|1|neckerchief'), Js('Girl Scout|2|cookie'), Js('Boy Scout|3|merit badge'), Js('Eagle Scout|4|merit badge'), Js('Bugbear|3|skin'), Js('Bugboar|3|tusk'), Js('Boogie|3|slime'), Js('Camel|2|hump'), Js('Carrion Crawler|3|egg'), Js('Catoblepas|6|neck'), Js('Centaur|4|rib'), Js('Centipede|0|leg'), Js('Cockatrice|5|wattle'), Js('Couatl|9|wing'), Js('Crayfish|0|antenna'), Js('Demogorgon|53|tentacle'), Js('Jubilex|17|gel'), Js('Manes|1|tooth'), Js('Orcus|27|wand'), Js('Succubus|6|bra'), Js('Vrock|8|neck'), Js('Hezrou|9|leg'), Js('Glabrezu|10|collar'), Js('Nalfeshnee|11|tusk'), Js('Marilith|7|arm'), Js('Balor|8|whip'), Js('Yeenoghu|25|flail'), Js('Asmodeus|52|leathers'), Js('Baalzebul|43|pants'), Js('Barbed Devil|8|flame'), Js('Bone Devil|9|hook'), Js('Dispater|30|matches'), Js('Erinyes|6|thong'), Js('Geryon|30|cornucopia'), Js('Malebranche|5|fork'), Js('Ice Devil|11|snow'), Js('Lemure|3|blob'), Js('Pit Fiend|13|seed'), Js('Anklyosaurus|9|tail'), Js('Brontosaurus|30|brain'), Js('Diplodocus|24|fin'), Js('Elasmosaurus|15|neck'), Js('Gorgosaurus|13|arm'), Js('Iguanadon|6|thumb'), Js('Megalosaurus|12|jaw'), Js('Monoclonius|8|horn'), Js('Pentasaurus|12|head'), Js('Stegosaurus|18|plate'), Js('Triceratops|16|horn'), Js('Tyranosauraus Rex|18|forearm'), Js('Djinn|7|lamp'), Js('Doppleganger|4|face'), Js('Black Dragon|7|*'), Js('Plaid Dragon|7|sporrin'), Js('Blue Dragon|9|*'), Js('Beige Dragon|9|*'), Js('Brass Dragon|7|pole'), Js('Tin Dragon|8|*'), Js('Bronze Dragon|9|medal'), Js('Chromatic Dragon|16|scale'), Js('Copper Dragon|8|loafer'), Js('Gold Dragon|8|filling'), Js('Green Dragon|8|*'), Js('Platinum Dragon|21|*'), Js('Red Dragon|10|cocktail'), Js('Silver Dragon|10|*'), Js('White Dragon|6|tooth'), Js('Dragon Turtle|13|shell'), Js('Dryad|2|acorn'), Js('Dwarf|1|drawers'), Js('Eel|2|sashimi'), Js('Efreet|10|cinder'), Js('Sand Elemental|8|glass'), Js('Bacon Elemental|10|bit'), Js('Porn Elemental|12|lube'), Js('Cheese Elemental|14|curd'), Js('Hair Elemental|16|follicle'), Js('Swamp Elf|1|lilypad'), Js('Brown Elf|1|tusk'), Js('Sea Elf|1|jerkin'), Js('Ettin|10|fur'), Js('Frog|0|leg'), Js('Violet Fungi|3|spore'), Js('Gargoyle|4|gravel'), Js('Gelatinous Cube|4|jam'), Js('Ghast|4|vomit'), Js('Ghost|10|*'), Js('Ghoul|2|muscle'), Js('Humidity Giant|12|drops'), Js('Beef Giant|11|steak'), Js('Quartz Giant|10|crystal'), Js('Porcelain Giant|9|fixture'), Js('Rice Giant|8|grain'), Js('Cloud Giant|12|condensation'), Js('Fire Giant|11|cigarettes'), Js('Frost Giant|10|snowman'), Js('Hill Giant|8|corpse'), Js('Stone Giant|9|hatchling'), Js('Storm Giant|15|barometer'), Js('Mini Giant|4|pompadour'), Js('Gnoll|2|collar'), Js('Gnome|1|hat'), Js('Goblin|1|ear'), Js('Grid Bug|1|carapace'), Js('Jellyrock|9|seedling'), Js('Beer Golem|15|foam'), Js('Oxygen Golem|17|platelet'), Js('Cardboard Golem|14|recycling'), Js('Rubber Golem|16|ball'), Js('Leather Golem|15|fob'), Js('Gorgon|8|testicle'), Js('Gray Ooze|3|gravy'), Js('Green Slime|2|sample'), Js('Griffon|7|nest'), Js('Banshee|7|larynx'), Js('Harpy|3|mascara'), Js('Hell Hound|5|tongue'), Js('Hippocampus|4|mane'), Js('Hippogriff|3|egg'), Js('Hobgoblin|1|patella'), Js('Homonculus|2|fluid'), Js('Hydra|8|gyrum'), Js('Imp|2|tail'), Js('Invisible Stalker|8|*'), Js('Iron Peasant|3|chaff'), Js('Jumpskin|3|shin'), Js('Kobold|1|penis'), Js('Leprechaun|1|wallet'), Js('Leucrotta|6|hoof'), Js('Lich|11|crown'), Js('Lizard Man|2|tail'), Js('Lurker|10|sac'), Js('Manticore|6|spike'), Js('Mastodon|12|tusk'), Js('Medusa|6|eye'), Js('Multicell|2|dendrite'), Js('Pirate|1|booty'), Js('Berserker|1|shirt'), Js('Caveman|2|club'), Js('Dervish|1|robe'), Js('Merman|1|trident'), Js('Mermaid|1|gills'), Js('Mimic|9|hinge'), Js('Mind Flayer|8|tentacle'), Js('Minotaur|6|map'), Js('Yellow Mold|1|spore'), Js('Morkoth|7|teeth'), Js('Mummy|6|gauze'), Js('Naga|9|rattle'), Js('Nebbish|1|belly'), Js('Neo-Otyugh|11|organ '), Js('Nixie|1|webbing'), Js('Nymph|3|hanky'), Js('Ochre Jelly|6|nucleus'), Js('Octopus|2|beak'), Js('Ogre|4|talon'), Js('Ogre Mage|5|apparel'), Js('Orc|1|snout'), Js('Otyugh|7|organ'), Js('Owlbear|5|feather'), Js('Pegasus|4|aileron'), Js('Peryton|4|antler'), Js('Piercer|3|tip'), Js('Pixie|1|dust'), Js('Man-o-war|3|tentacle'), Js('Purple Worm|15|dung'), Js('Quasit|3|tail'), Js('Rakshasa|7|pajamas'), Js('Rat|0|tail'), Js('Remorhaz|11|protrusion'), Js('Roc|18|wing'), Js('Roper|11|twine'), Js('Rot Grub|1|eggsac'), Js('Rust Monster|5|shavings'), Js('Satyr|5|hoof'), Js('Sea Hag|3|wart'), Js('Silkie|3|fur'), Js('Shadow|3|silhouette'), Js('Shambling Mound|10|mulch'), Js('Shedu|9|hoof'), Js('Shrieker|3|stalk'), Js('Skeleton|1|clavicle'), Js('Spectre|7|vestige'), Js('Sphinx|10|paw'), Js('Spider|0|web'), Js('Sprite|1|can'), Js('Stirge|1|proboscis'), Js('Stun Bear|5|tooth'), Js('Stun Worm|2|trode'), Js('Su-monster|5|tail'), Js('Sylph|3|thigh'), Js('Titan|20|sandal'), Js('Trapper|12|shag'), Js('Treant|10|acorn'), Js('Triton|3|scale'), Js('Troglodyte|2|tail'), Js('Troll|6|hide'), Js('Umber Hulk|8|claw'), Js('Unicorn|4|blood'), Js('Vampire|8|pancreas'), Js('Wight|4|lung'), Js("Will-o'-the-Wisp|9|wisp"), Js('Wraith|5|finger'), Js('Wyvern|7|wing'), Js('Xorn|7|jaw'), Js('Yeti|4|fur'), Js('Zombie|2|forehead'), Js('Wasp|0|stinger'), Js('Rat|1|tail'), Js('Bunny|0|ear'), Js('Moth|0|dust'), Js('Beagle|0|collar'), Js('Midge|0|corpse'), Js('Ostrich|1|beak'), Js('Billy Goat|1|beard'), Js('Bat|1|wing'), Js('Koala|2|heart'), Js('Wolf|2|paw'), Js('Whippet|2|collar'), Js('Uruk|2|boot'), Js('Poroid|4|node'), Js('Moakum|8|frenum'), Js('Fly|0|*'), Js('Hogbird|3|curl'), Js('Wolog|4|lemma')]))
PyJs_LONG_17_()
var.get('K').put('MonMods', Js([Js('-4 fœtal *'), Js('-4 dying *'), Js('-3 crippled *'), Js('-3 baby *'), Js('-2 adolescent'), Js('-2 very sick *'), Js('-1 lesser *'), Js('-1 undernourished *'), Js('+1 greater *'), Js('+1 * Elder'), Js('+2 war *'), Js('+2 Battle-*'), Js('+3 Were-*'), Js('+3 undead *'), Js('+4 giant *'), Js('+4 * Rex')]))
var.get('K').put('OffenseBad', Js([Js('Dull|-2'), Js('Tarnished|-1'), Js('Rusty|-3'), Js('Padded|-5'), Js('Bent|-4'), Js('Mini|-4'), Js('Rubber|-6'), Js('Nerf|-7'), Js('Unbalanced|-2')]))
var.get('K').put('DefenseBad', Js([Js('Holey|-1'), Js('Patched|-1'), Js('Threadbare|-2'), Js('Faded|-1'), Js('Rusty|-3'), Js('Motheaten|-3'), Js('Mildewed|-2'), Js('Torn|-3'), Js('Dented|-3'), Js('Cursed|-5'), Js('Plastic|-4'), Js('Cracked|-4'), Js('Warped|-3'), Js('Corroded|-3')]))
def PyJs_LONG_18_(var=var):
    return var.get('K').put('Races', Js([Js('Half Orc|HP Max'), Js('Half Man|CHA'), Js('Half Halfling|DEX'), Js('Double Hobbit|STR'), Js('Hob-Hobbit|DEX,CON'), Js('Low Elf|CON'), Js('Dung Elf|WIS'), Js('Talking Pony|MP Max,INT'), Js('Gyrognome|DEX'), Js('Lesser Dwarf|CON'), Js('Crested Dwarf|CHA'), Js('Eel Man|DEX'), Js('Panda Man|CON,STR'), Js('Trans-Kobold|WIS'), Js('Enchanted Motorcycle|MP Max'), Js("Will o' the Wisp|WIS"), Js('Battle-Finch|DEX,INT'), Js('Double Wookiee|STR'), Js('Skraeling|WIS'), Js('Demicanadian|CON'), Js('Land Squid|STR,HP Max')]))
PyJs_LONG_18_()
def PyJs_LONG_19_(var=var):
    return var.get('K').put('Klasses', Js([Js('Ur-Paladin|WIS,CON'), Js('Voodoo Princess|INT,CHA'), Js('Robot Monk|STR'), Js('Mu-Fu Monk|DEX'), Js('Mage Illusioner|INT,MP Max'), Js('Shiv-Knight|DEX'), Js('Inner Mason|CON'), Js('Fighter/Organist|CHA,STR'), Js('Puma Burgular|DEX'), Js('Runeloremaster|WIS'), Js('Hunter Strangler|DEX,INT'), Js('Battle-Felon|STR'), Js('Tickle-Mimic|WIS,INT'), Js('Slow Poisoner|CON'), Js('Bastard Lunatic|CON'), Js('Lowling|WIS'), Js('Birdrider|WIS'), Js('Vermineer|INT')]))
PyJs_LONG_19_()
var.get('K').put('Titles', Js([Js('Mr.'), Js('Mrs.'), Js('Sir'), Js('Sgt.'), Js('Ms.'), Js('Captain'), Js('Chief'), Js('Admiral'), Js('Saint')]))
var.get('K').put('ImpressiveTitles', Js([Js('King'), Js('Queen'), Js('Lord'), Js('Lady'), Js('Viceroy'), Js('Mayor'), Js('Prince'), Js('Princess'), Js('Chief'), Js('Boss'), Js('Archbishop')]))
pass


# Add lib to the module scope
conf = var.to_python()