import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import Profile from './components/Profile';
import NotFound from './components/NotFound';

function CareerApp() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/profile" component={Profile} />
        <Route component={NotFound} />
      </Switch>
    </Router>
  );
}

export default CareerApp;

In the Home component, you might have a form for users to input their interests and skills, which you can use to make recommendations:

Home.jsx
import React, { useState } from 'react';

function Home() {
  const [interests, setInterests] = useState('');
  const [skills, setSkills] = useState('');

  const handleRecommendation = () => {
    // Make API call to backend with user interests and skills
    // Receive recommendations and update UI accordingly
  };

  return (
    <div>
      <h1>Welcome to Career Guidance App</h1>
      <label>
        Interests:
        <input type="text" value={interests} onChange={(e) => setInterests(e.target.value)} />
      </label>
      <label>
        Skills:
        <input type="text" value={skills} onChange={(e) => setSkills(e.target.value)} />
      </label>
      <button onClick={handleRecommendation}>Get Recommendations</button>
    </div>
  );
}

export default Home;