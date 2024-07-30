import React from "react";
import { useNavigate } from "react-router-dom";
import UserPool from "../userpool";

function Dashboard() {
  const navigate = useNavigate();

  const handleLogout = () => {
    const user = UserPool.getCurrentUser();
    if (user) {
      user.signOut();
    }
    navigate("/login");
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-950">
      <div className="w-full max-w-md p-8 space-y-3 rounded-xl bg-white shadow-lg">
        <h1 className="text-3xl font-bold text-center text-indigo-800">
          Job Matching
        </h1>
        <button
          onClick={handleLogout}
          className="w-full py-2 px-4 text-white font-semibold bg-indigo-800 rounded-md hover:bg-indigo-900 focus:outline-none"
        >
          Logout
        </button>
      </div>
    </div>
  );
}

export default Dashboard;
