import Artist from '~/utils/types/Artists';
import Genre from '~/utils/types/Genres';
interface Song {
    artists: Artist[];
    filename: string;
    genre: Genre;
    plays: [];
    thumbnail: string;
    title: string;
    uniqid: string;
    yt_url: string;
};

export default Song;