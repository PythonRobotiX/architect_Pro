import React from 'react';
import ReactDOM from 'react-dom';
import './styles.css';
import './scripts.js';

function App() {
  return (
    <div>
      <header>
        <div className="language-switcher">
          <button id="toggle-lang" onClick={toggleLanguage}>EN/FA</button>
        </div>
      </header>

      <div className="container">
        <nav className="sidebar left">
          <div className="photo-placeholder-sidebar">
            <img src="arya-photo.jpg" alt="Arya's Photo" />
          </div>
          <ul>
            <li><a href="#biography" onClick={() => showSection('biography')}>Arya's Biography</a></li>
            <li><a href="#research" onClick={() => showSection('research')}>Research & Development (R&D)</a></li>
            <li><a href="#portfolio" onClick={() => showSection('portfolio')}>Arya's Portfolio</a></li>
            <li><a href="#creator" onClick={() => showSection('creator')}>Architect's Portfolio Creator</a></li>
            <li><a href="#projects" onClick={() => showSection('projects')}>We Accept Orders and Projects</a></li>
            <li><a href="#contact" onClick={() => showSection('contact')}>Contact Us</a></li>
            <li><a href="#about" onClick={() => showSection('about')}>About Us</a></li>
          </ul>
        </nav>

        <main className="content">
          <div className="welcome-message">
            <h1>Welcome to Arya Piranviseh's Official Website</h1>
          </div>
          <div className="center-photo">
            <div className="photo-placeholder">
              <img src="architect-photo.jpg" alt="Architect" />
              <div className="motto">Designing Tomorrow's Spaces, Today.</div>
            </div>
          </div>
          <div className="top-news">
            <h2>Today's Top News</h2>
            <ul>
              <li><a href="https://www.architecturaldigest.com" target="_blank">Title of Architectural News 1</a></li>
              <li><a href="https://www.dezeen.com" target="_blank">Title of Architectural News 2</a></li>
              <li><a href="https://www.archdaily.com" target="_blank">Title of Architectural News 3</a></li>
            </ul>
          </div>
          <section id="biography" style={{ display: 'none' }}>
            <h1>Arya's Biography</h1>
            <div id="biography-content">
              <p>Arya Piranviseh was born on March 26, 1995, in Tehran, Iran. He is a dedicated architect, continuously honing his skills in software such as AutoCAD, Grasshopper, Rhino, and the Python programming language. Arya has undertaken extensive projects in construction, renovation, floor planning, and interior and exterior design.</p>
              <p>In 2022, Arya earned his Master's degree in Architecture from the Shaheed Beheshti School of Architecture in Tehran. He is currently working on his doctoral thesis while simultaneously managing his own architectural projects. In addition to his personal endeavors, Arya is enthusiastic about collaborating with other architects and contributing to their work.</p>
              <p>Arya is passionate about acquiring new projects through this website. To place your orders, please visit the "We Accept Orders and Projects" section.</p>
            </div>
          </section>
          <section id="research" style={{ display: 'none' }}>
            <h1>Research & Development (R&D)</h1>
            <div className="projects-grid">
              <div className="project">
                <img src="thumbnail1.jpg" alt="Project 1" />
                <p>Project Name 1 (2021)</p>
                <div className="project-files">
                  <a href="project1-1.mp4" target="_blank">Video 1</a>
                  <a href="project1-2.mpeg" target="_blank">Video 2</a>
                  <a href="project1-3.mov" target="_blank">Video 3</a>
                  <a href="project1-4.pdf" target="_blank">Document 1</a>
                  <a href="project1-5.jpg" target="_blank">Image 1</a>
                  <a href="project1-6.jpeg" target="_blank">Image 2</a>
                  <a href="project1-7.png" target="_blank">Image 3</a>
                </div>
              </div>
              <div className="project">
                <img src="thumbnail2.jpg" alt="Project 2" />
                <p>Project Name 2 (2020)</p>
                <div className="project-files">
                  <a href="project2-1.mp4" target="_blank">Video 1</a>
                  <a href="project2-2.mpeg" target="_blank">Video 2</a>
                  <a href="project2-3.mov" target="_blank">Video 3</a>
                  <a href="project2-4.pdf" target="_blank">Document 1</a>
                  <a href="project2-5.jpg" target="_blank">Image 1</a>
                  <a href="project2-6.jpeg" target="_blank">Image 2</a>
                  <a href="project2-7.png" target="_blank">Image 3</a>
                </div>
              </div>
              <div className="project">
                <img src="thumbnail3.jpg" alt="Project 3" />
                <p>Project Name 3 (2019)</p>
                <div className="project-files">
                  <a href="project3-1.mp4" target="_blank">Video 1</a>
                  <a href="project3-2.mpeg" target="_blank">Video 2</a>
                  <a href="project3-3.mov" target="_blank">Video 3</a>
                  <a href="project3-4.pdf" target="_blank">Document 1</a>
                  <a href="project3-5.jpg" target="_blank">Image 1</a>
                  <a href="project3-6.jpeg" target="_blank">Image 2</a>
                  <a href="project3-7.png" target="_blank">Image 3</a>
                </div>
              </div>
              {/* Add more projects as needed */}
            </div>
          </section>
          <section id="portfolio" style={{ display: 'none' }}>
            <h1>Arya's Portfolio</h1>
            {/* Portfolio content */}
          </section>
          <section id="creator" style={{ display: 'none' }}>
            <h1>Architect's Portfolio Creator</h1>
            {/* Portfolio creator content */}
          </section>
          <section id="projects" style={{ display: 'none' }}>
            <h1>We Accept Orders and Projects</h1>
            {/* Projects submission content */}
          </section>
          <section id="contact" style={{ display: 'none' }}>
            <h1>Contact Us</h1>
            <form>
              <p>Please fill out the following form:</p>
              <label htmlFor="name">Name:</label>
              <input type="text" id="name" name="name" required /><br />
              <label htmlFor="tel">Tel # (with country code):</label>
              <input type="tel" id="tel" name="tel" required /><br />
              <label htmlFor="email">Email address (optional):</label>
              <input type="email" id="email" name="email" /><br />
              <label htmlFor="file">Upload your files (please no more than 25 MBs and only in these formats: .pdf, .mpeg, .mp4, .mov, .png, .jpeg, .jpg):</label>
              <input type="file" id="file" name="file" accept=".pdf, .mpeg, .mp4, .mov, .png, .jpeg, .jpg" multiple /><br />
              <label htmlFor="comments">Write your question or comment here:</label>
              <textarea id="comments" name="comments" rows="4" cols="50" required></textarea><br />
              <input type="submit" value="Submit" />
            </form>
          </section>
          <section id="about" style={{ display: 'none' }}>
            <h1>About Us</h1>
            <div id="about-content">
              <p>With the recent advent of energy resources such as solar panels and the emergence of new rechargeable battery cells, we are committed to building and designing floors and spaces that utilize sustainable energy.</p>
            </div>
          </section>
        </main>

        <nav className="sidebar right">
          <ul>
            <li><a href="#photo-gallery" onClick={() => showSection('photo-gallery')}>Photo Gallery</a></li>
            <li><a href="#landmark-structures" onClick={() => showSection('landmark-structures')}>Landmark Structures</a></li>
            <li><a href="#workshop" onClick={() => showSection('workshop')}>Workshop</a></li>
            <li><a href="#linkedin" onClick={() => showSection('linkedin')}>LinkedIn</a></li>
            <li><a href="#instagram" onClick={() => showSection('instagram')}>Instagram</a></li>
          </ul>
        </nav>
      </div>

      <footer>
        <p>&copy; 2024 Arya Piranviseh. All rights reserved.</p>
      </footer>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
