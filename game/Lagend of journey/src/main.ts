import './style.css'

interface GameState {
  level: number
  exp: number
  gold: number
  monsterHp: number
  monsterIndex: number
}

const monsters = [
  'Slime Forest', 
  'Wild Goblin', 
  'Dark Wolf', 
  'Skeleton Knight', 
  'Ancient Dragon', 
]

const saved =
localStorage.getItem('legend-server')

const state: GameState = saved ? JSON.parse(saved)
: {
  level: 1,
  exp: 0,
  gold: 0,
  monsterHp: 60,
  monsterIndex: 0
}

const app = document.querySelector<HTMLDivElement>('#app')

if (!app) throw new Error('App element not found')

  function getMaxHp() {
    return 60 + state.monsterIndex * 35
  }

  function getRequiredExp() {
    return state.level * 100
  }

  function savegame(){

    localStorage.setItem('legend-save', JSON.stringify(state))
  }

  function attack() {
    const damage = 10 + state.level * 2

    state.monsterHp -= damage

    if (state.monsterHp <= 0) {
      state.gold += 25
      state.exp += 40

      if (state.exp >= getRequiredExp()) {
        state.exp -= getRequiredExp()
        state.level++
      }

      state.monsterIndex = (state.monsterIndex + 1) % monsters.length

      state.monsterHp = getMaxHp()
    }

    savegame()
    render()
  }

  function render() {
    const monster = monsters[state.monsterIndex]
    const maxHp = getMaxHp()
    const expNeeded = getRequiredExp()
    
    app!.innerHTML = `
    <header>
    <h1> LEGEND OF JOURNEY</h1>
    <p>An Endless Fantasy Advanture</p>
    </header>
    
    <main>
    <section class="player-card">
    <h2>Advanture</h2>
    <h3>Level ${state.level}</h3>
    
    <p>EXP: ${state.exp} / $ {expNeeded}</p>
    <div class= "bar">
    <div style= "width:${Math.min(state.exp / expNeeded * 100, 100)}%"></div>
    </div>
    
    <p>Gold: ${state.gold} G</p>
    </section>
    
    <section class="battle-card">
    <p class="location">FOREST OF BEGINNING</p>`
  }