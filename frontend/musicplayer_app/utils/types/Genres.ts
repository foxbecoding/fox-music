import Song from '~/utils/types/Songs';
interface Genre {
    name: string;
    uniqid: string;
    songs: Song[]
};

export default Genre;