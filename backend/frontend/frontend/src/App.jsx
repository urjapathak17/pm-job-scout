import React, { useEffect, useState } from 'react';

export default function App() {
  const [jobs, setJobs] = useState([]);
  const [bookmarkedJobs, setBookmarkedJobs] = useState([]);

  useEffect(() => {
    fetch('/data/jobs.json')
      .then(res => res.json())
      .then(data => setJobs(data.jobs));
    setBookmarkedJobs(JSON.parse(localStorage.getItem('bookmarkedJobs') || '[]'));
  }, []);

  const toggleBookmark = jobId => {
    const bookmarks = JSON.parse(localStorage.getItem('bookmarkedJobs') || '[]');
    const isBookmarked = bookmarks.includes(jobId);
    let newBookmarks;
    if (isBookmarked) {
      newBookmarks = bookmarks.filter(id => id !== jobId);
    } else {
      newBookmarks = [...bookmarks, jobId];
    }
    localStorage.setItem('bookmarkedJobs', JSON.stringify(newBookmarks));
    setBookmarkedJobs(newBookmarks);
  };

  return (
    <div>
      <header className="bg-blue-600 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="text-center">
            <h1 className="text-4xl font-bold text-white mb-2">🚀 PM Job Scout</h1>
            <p className="text-gray-100 mb-4">AI-powered Product Manager job aggregator with authenticity verification</p>
          </div>
        </div>
      </header>
      <div className="my-6 flex justify-center">
        <button className="px-6 py-3 bg-purple-600 text-white rounded-lg hover:bg-purple-700 flex items-center gap-2">
          <span className="w-4 h-4">🔍</span> Search
        </button>
      </div>
      <input type="text" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500" placeholder="Type your search..." />
      <div className="mt-8">
        {jobs.map(job => (
          <div key={job.id} className="p-4 border-b flex items-center">
            <span className="px-3 py-1 bg-purple-100 text-purple-800 text-sm rounded-full">{job.workType}</span>
            <a href={job.applyUrl} target="_blank" rel="noopener noreferrer" className="bg-purple-600 text-white px-6 py-2 rounded-lg hover:bg-purple-700 transition-colors text-sm font-medium ml-4">
              Apply Now →
            </a>
            <button onClick={() => toggleBookmark(job.id)} className={`p-2 rounded ml-4 ${bookmarkedJobs.includes(job.id) ? 'text-red-500' : 'text-gray-400'}`}>
              {bookmarkedJobs.includes(job.id) ? '❤️' : '🤍'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

Add React App.jsx main component

