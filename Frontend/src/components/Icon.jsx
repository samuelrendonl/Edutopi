const paths = {
  sparkles: <><path d="m12 2 1.45 5.55L19 9l-5.55 1.45L12 16l-1.45-5.55L5 9l5.55-1.45L12 2Z"/><path d="m19 15 .7 2.3L22 18l-2.3.7L19 21l-.7-2.3L16 18l2.3-.7L19 15Z"/></>,
  calculator: <><rect x="5" y="3" width="14" height="18" rx="2"/><rect x="8" y="6" width="8" height="3" rx="1"/><path d="M8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01M16 17h.01" strokeWidth="2.4"/></>,
  book: <><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5v-16Z"/><path d="M4 5.5v16M8 7h8M8 11h8"/></>,
  leaf: <><path d="M20 4C10 4 4 8.5 4 15c0 3 2 5 5 5 6.5 0 11-6 11-16Z"/><path d="M4 20c3-5 7-8 13-10"/></>,
  globe: <><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9S14.5 18.5 12 21c-2.5-2.5-3.5-5.5-3.5-9S9.5 5.5 12 3Z"/></>,
  rainbow: <><path d="M3 18a9 9 0 0 1 18 0"/><path d="M6 18a6 6 0 0 1 12 0M9 18a3 3 0 0 1 6 0"/></>,
  rocket: <><path d="M14 4c3-2 5-1 5-1s1 2-1 5l-5 5-4-4 5-5Z"/><path d="m9 9-4 1 5 5 1-4M14 14l-1 5-5-5 4-1"/><circle cx="15.5" cy="6.5" r="1"/></>,
  family: <><circle cx="12" cy="6" r="3"/><circle cx="5.5" cy="9" r="2"/><circle cx="18.5" cy="9" r="2"/><path d="M5 20v-3a7 7 0 0 1 14 0v3M2 19v-2a3.5 3.5 0 0 1 3-3.45M22 19v-2a3.5 3.5 0 0 0-3-3.45"/></>,
  game: <><path d="M5 9h14a4 4 0 0 1 3.8 5.25l-1.2 3.6a2 2 0 0 1-3.65.35L16.5 16h-9l-1.45 2.2a2 2 0 0 1-3.65-.35l-1.2-3.6A4 4 0 0 1 5 9Z"/><path d="M7 12v4M5 14h4M17 13h.01M19 15h.01" strokeWidth="2"/></>,
  check: <path d="m5 12 4 4L19 6" strokeWidth="2.5"/>,
  target: <><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/></>,
  lightbulb: <><path d="M9 18h6M10 21h4"/><path d="M8 14.5A6 6 0 1 1 16 14c-.7.7-1 1.4-1 2H9c0-.7-.3-1.2-1-1.5Z"/></>,
  telescope: <><path d="m5 7 12-4 2 6-12 4-2-6Z"/><path d="m9 13-3 8M14 12l3 9M7 21h5M15 21h5"/></>,
  sun: <><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></>,
  cloud: <path d="M7 18h10a4 4 0 0 0 .6-7.95A6 6 0 0 0 6.1 9.1 4.5 4.5 0 0 0 7 18Z"/>,
  planet: <><circle cx="12" cy="12" r="6"/><path d="M3 15c2.5-3 7-4 11-2s5 3 7 1"/></>,
  star: <path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-2.9-5.6 2.9 1.1-6.2L3 9.6l6.2-.9L12 3Z"/>,
  hand: <><path d="M7 12V6.5a1.5 1.5 0 0 1 3 0V11"/><path d="M10 11V4.5a1.5 1.5 0 0 1 3 0V11"/><path d="M13 11V6a1.5 1.5 0 0 1 3 0v6"/><path d="M16 12V9a1.5 1.5 0 0 1 3 0v5c0 4-2.5 7-6.5 7h-1C8 21 5 18 5 14.5v-1a1.5 1.5 0 0 1 3 0V15"/></>,
  users: <><circle cx="9" cy="8" r="3"/><path d="M3 20v-1a6 6 0 0 1 12 0v1"/><path d="M16 5.5a3 3 0 0 1 0 5.8M18 14a5 5 0 0 1 3 4.5V20"/></>,
  heart: <path d="M20.8 8.8c0 5.2-8.8 10.2-8.8 10.2S3.2 14 3.2 8.8A4.6 4.6 0 0 1 12 6.4a4.6 4.6 0 0 1 8.8 2.4Z"/>,
  smile: <><circle cx="12" cy="12" r="9"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01" strokeWidth="2.2"/></>,
  fox: <><path d="m5 8 1-4 4 2a7 7 0 0 1 4 0l4-2 1 4v5a7 7 0 0 1-14 0V8Z"/><path d="m8 13 4 3 4-3M9 10h.01M15 10h.01" strokeWidth="2"/></>,
  flag: <><path d="M5 21V4"/><path d="M5 5c5-3 8 3 14 0v9c-6 3-9-3-14 0"/></>,
  medal: <><circle cx="12" cy="15" r="5"/><path d="m9 11-2-8 5 3 5-3-2 8M10 15h4M12 13v4"/></>,
  search: <><circle cx="10.8" cy="10.8" r="6.8"/><path d="m16 16 5 5"/></>,
  clock: <><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></>,
  arrowRight: <><path d="M5 12h14M13 6l6 6-6 6"/></>,
};

export default function Icon({ name, size = 24, strokeWidth = 1.8, className = "" }) {
  return <svg className={`ui-icon ${className}`} width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={strokeWidth} strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">{paths[name] || paths.sparkles}</svg>;
}
