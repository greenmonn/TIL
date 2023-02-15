# JSMobileConf Day 1
#conference #javascript 

## Keynote: Evolution of the JavaScript
### From 2007: web -> smartphone

### 2009 - 2010: mobile web environment

### 2013: “Web hybrid” vs. “100% Native”
### 2015: React native & NativeScript

### NativeScript
- Plugins / external contributions

- Instant Start CLI framework
	- run a CLI, simple command, simplify startup
- HMR(Hot Module Replacement)
	- without reloading, refresh
	- maintain app state as code changes
- Reusing existing web technology and resource
- Code reuse: web& mobile code sharing

### 2018: Sharing code between Web & Mobile
- Still hard problem: offline, data sync, CD, legacy code..

> Be ready for the future  
> Bet on Javascript (again)  

## Responsive Design: Beyond Our Devices
- Digital Design
- Pages to Patterns
- Layout for all the devices

- a network of content rearranged by all size of display
- Design the **priority** not the layout: content hierarchy before layout
- “teaser”
- flex-direction
- Feature Queries: @supports Rule
	- “Support” doesn’t mean the exactly same experience on all devices
- Conditionally enhanced layout (`.has-flex`, .`has-flex-wrap`)

> Like cars designed to perform in extreme heat or on icy road, web should treat non-ideal environment.  

Input method / screen size / network speed / network condition

Pattern library/Style guide: [Style Guide](https://www.starbucks.com/static/reference/styleguide/)

> We should start with language, not interfaces.  

- Naming the element in the pattern library helps **consistency** and avoid **duplications** with other designers
- We need consistent and meaningful terms for the design pattern

[Responsive Design: Patterns & Principles: Ethan Marcotte: 9781937557331: Amazon.com: Books](https://www.amazon.com/Responsive-Design-Principles-Ethan-Marcotte/dp/1937557332)

## Blockchain Crash Course
By [Crescendo](https://getcrescendo.co/) CTO

- Centralized System
- Build trust, consistency
- Set of same data
- PrevHash: immutability, one-way hash
- Add transaction -> consensus protocol [vote]

> Network protocol: how do peers communicate  
> Consensus protocol: how are decisions made  
> 	- Proof of Work: difficult puzzle  
> 	- Proof of Stake: stake -> ownership  
> Transaction protocol: what makes transactions valid  

- Use case: Spotify / MedicalChain: ‘누가’ 로열티를 받을지, product의 유통 과정

- Blockchain with JS
	- JS as a front-end
		- Solidity
		- Ethereum
	- JS driving the car
		- Lotion.js: [GitHub - keppel/lotion: ✨ Smooth, easy blockchain apps ✨](https://github.com/keppel/lotion)
		- Tendermint

[Blockchain community - Blockgeeks](https://blockgeeks.com/)

@thetrendytechie
[GitHub - thetrendytechie/bed-and-blockchain: Simple decentralized booking system dapp built with Solidity and Truffle](https://github.com/thetrendytechie/bed-and-blockchain)

## One Project, One Language, Three Apps
[Code Sharing Introduction](https://docs.nativescript.org/angular/code-sharing/intro)

## Boosting Your Development Experience with Webpack and Hot Module Replacement
- Hot Module Replacement
- TNS preview: no Android/iOS setup
- Webpack
	- Every Javascript file is a module
	- Every HTML file is a module
	- Every CSS file is a module

- Angular - native script no HMR default
- State Management
	- Redux, ngRX, ngXS, akita

[Tracking🔥Hot Module Replacement with webpack · Issue #6398 · NativeScript/NativeScript · GitHub](https://github.com/NativeScript/NativeScript/issues/6398)

## Boosting the IoT to Your Will with Javascript
- Smartfin([Smartfin - Surfrider Foundation](https://www.surfrider.org/programs/smartfin))
- Connectivity in sensors
- Get data from the sensors -> build an application
- Particle Cloud: [GitHub - particle-iot/particle-api-js: JS Library for the Particle API](https://github.com/particle-iot/particle-api-js)
- NativeScript Particle Plugin

- Building IoT cloud apps
	1. Cloud backhaul (AWS IoT, google IoT)
	2. Cloud Workflow (NODE-RED, LOSANT)
	3. Cloud processing (IBM Watson)

## Lean Native
1. Pre-build
	1. Validate problem
		- pain level metric
	2. Validate solution
		- enthusiasm level + referrals(bonus) + writing a check(bonus!! - B2B)   
		- it is worth to introduce to someone
	3. Validate channel: landing page, Sales/Marketing

2. MVP
	1. Early Adopters
	2. Validate acquisition(total cost/acquiring customers)
	3. Determine value: know your cohorts

3. Growth
	1. Channel Optimization
	2. Acquisition loops
	3. Retention loops














